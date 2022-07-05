from django.contrib import admin
from .models import *


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user", "email"]
    search_fields = ["user", "email"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['group', "name", "price", "unit", "comment"]
    search_fields = ['group', "name", "price", "unit", "comment"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', "customer_info"]
    search_fields = ['customer_name', "customer_info"]


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['customer', "date_saved"]
    search_fields = ['customer', "date_saved"]


class DocumentItemAdmin(admin.ModelAdmin):
    list_display = ['order', "service", "quantity"]
    search_fields = ['order', "service", "quantity"]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Quote, DocumentAdmin)
admin.site.register(QuoteItem, DocumentItemAdmin)
