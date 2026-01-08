from django.db import models

class DailySales(models.Model):
    date = models.DateField(null=True, blank=True)
    client_id = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=100, blank=True)
    value_sale = models.IntegerField(null=True, blank=True)
