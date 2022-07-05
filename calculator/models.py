from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, default="Karen")
	email = models.EmailField(max_length=20)

	def __str__(self):
		return self.email


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
	price = models.DecimalField(decimal_places=2, max_digits=6)
	unit = models.CharField(max_length=15, choices=UNIT_CHOICES, default=NA)
	comment = models.CharField(max_length=250)

	def __str__(self):
		return self.name


class Customer(models.Model):
	customer_name = models.CharField(max_length=100)
	customer_info = models.CharField(max_length=100)

	def __str__(self):
		return self.customer_name


class Quote(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	date_saved = models.DateTimeField(auto_now=True)
	employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
	comment = models.CharField(max_length=300, null=True)

	def __str__(self):
		return str(self.customer.customer_name)


class QuoteItem(models.Model):
	order = models.ForeignKey(Quote, on_delete=models.SET_NULL, null=True)
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
