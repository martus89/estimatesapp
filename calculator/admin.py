from . import models
from django.contrib import admin


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["group", "name"]
    }
    list_display = ["id", 'group', "name", "slug", "price", "unit", "last_update", "comment"]
    list_per_page = 15
    search_fields = ['group__startswith', "name__startswith", "comment__startswith"]
    list_filter = ['group', 'last_update']

    # not working? ;(
    # def quote_count(self, obj):
    #     return obj.service_set.count()


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", 'customer_name', "quote_count", "customer_info"]
    list_editable = ['customer_info']
    list_per_page = 15
    search_fields = ['customer_name__startswith', "customer_info__startswith"]

    def quote_count(self, obj):
        return obj.quote_set.count()


class QuoteItemInLine(admin.TabularInline):
    model = models.QuoteItem
    readonly_fields = ["service_group", "service_unit", "service_price", "line_total"]
    list_display = ["id", "name", "quantity"]
    list_per_page = 15
    search_fields = ["service_group", "name"]
    autocomplete_fields = ['name']
    extra = 0
    min_num = 1
    max_num = 10

    def service_group(self, obj):
        return obj.name.group

    def service_unit(self, obj):
        return obj.name.unit

    def service_price(self, obj):
        return obj.name.price

    def line_total(self, obj):
        return obj.name.price * obj.quantity


@admin.register(models.Quote)
class QuoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ["customer", "slug"]
    }

    readonly_fields = ["date_saved"]
    list_display = ["id", "date_saved", 'customer', "user"]
    list_per_page = 15
    search_fields = ['customer', "user"]
    autocomplete_fields = ['customer']
    inlines = [QuoteItemInLine]
    list_filter = ['date_saved', 'user']
