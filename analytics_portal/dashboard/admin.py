from django.contrib import admin

from dashboard.models import DailySales

@admin.register(DailySales)
class DailySalesAdmin(admin.ModelAdmin):
    list_display = ('date', 'client_id', 'product', 'value_sale')
