from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from estimates.utils import slugify_instance_customer
# Create your models here.


class Service(models.Model):
	"""Class stores all services currently on offer"""

	NA = "n/a"
	M2 = "m2"
	T = "t"
	H = "h"
	KM = "km"
	M3 = "m3"
	ITEM = "Item"

	UNIT_CHOICES = [
		(NA, NA),
		(M2, M2),
		(T, T),
		(H, H),
		(KM, KM),
		(M3, M3),
		(ITEM, ITEM)
	]

	TRANSPORT = "Transport"
	CONCRETE = "Concrete"
	RENTAL = "Rental"
	PAVING = "Paving"
	CHIPPING = "Chipping"
	OTHER = "Other"

	GROUP_CHOICES = [
		(TRANSPORT, TRANSPORT),
		(CONCRETE, CONCRETE),
		(RENTAL, RENTAL),
		(PAVING, PAVING),
		(CHIPPING, CHIPPING),
		(OTHER, OTHER),
	]
	group = models.CharField(max_length=15, choices=GROUP_CHOICES, default=OTHER)
	name = models.CharField(max_length=200)
	priceEUR = models.DecimalField(decimal_places=2, max_digits=6, validators=[MinValueValidator(1)], null=True)
	unit = models.CharField(max_length=15, choices=UNIT_CHOICES, default=NA)
	comment = models.CharField(max_length=250, blank=True, null=True)
	last_update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['name']


class Customer(models.Model):
	"""Class stores all customers currently in cooperation"""
	customer_name = models.CharField(max_length=100)
	customer_info = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return str(self.customer_name)


class QuoteQuerySet(models.QuerySet):
	def search(self, query=None):
		if query is None or query == "":
			return self.none()
		lookups = Q(customer__icontains=query) | Q(content__icontains=query)
		return self.filter(lookups)


class QuoteManager(models.Manager):
	def get_queryset(self):
		return QuoteQuerySet(self.model, using=self._db)

	def search(self, query=None):
		return self.get_queryset().search(query=query)


class Quote(models.Model):
	"""Class stores all quotes generated for customers"""
	date_saved = models.DateTimeField(auto_now=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True, blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, auto_created=True)
	comment = models.CharField(max_length=300, null=True, blank=True)

	objects = QuoteManager()

	@property
	def name(self):
		return self.date_saved

	def get_absolute_url(self):
		return reverse("quote_detail", kwargs={"slug": self.slug})

	def get_quoteitems_children(self):
		return self.quoteitem_set.all()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)


def quote_pre_save(sender, instance, *args, **kwargs):
	if instance.slug is None:
		slugify_instance_customer(instance, save=False)


pre_save.connect(quote_pre_save, sender=Quote)


def quote_post_save(sender, instance, created, *args, **kwargs):
	if created:
		slugify_instance_customer(instance, save=True)


post_save.connect(quote_post_save, sender=Quote)


class QuoteItem(models.Model):
	"""Class created to store single items (single lines) per quote"""
	quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
	name = models.ForeignKey(Service, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1, blank=True, null=False)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return self.quote.get_absolute_url()
