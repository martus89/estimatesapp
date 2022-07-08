from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator


class Service(models.Model):

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
	slug = models.SlugField()
	price = models.DecimalField(decimal_places=2, max_digits=6, validators=[MinValueValidator(1)], null=True)
	unit = models.CharField(max_length=15, choices=UNIT_CHOICES, default=NA)
	comment = models.CharField(max_length=250, blank=True, null=True)
	last_update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ['name']


class Customer(models.Model):
	customer_name = models.CharField(max_length=100)
	customer_info = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return str(self.customer_name)


class Quote(models.Model):
	date_saved = models.DateTimeField(auto_now=True)
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	slug = models.SlugField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, auto_created=True)
	comment = models.CharField(max_length=300, null=True, blank=True)

	def __str__(self):
		return str(self.customer)


class QuoteItem(models.Model):
	quote = models.ForeignKey(Quote, on_delete=models.PROTECT)
	name = models.ForeignKey(Service, on_delete=models.PROTECT)
	quantity = models.PositiveIntegerField(default=1, blank=True, null=False)

	def __str__(self):
		return str(self.name)
