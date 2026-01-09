from django.db import models

class DailySales(models.Model):
    """ Modelo para la tabla de datos de ventas diarias """
    date = models.DateField(null=True, blank=True)
    client_id = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=100, blank=True)
    value_sale = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'ventas_diarias'
        verbose_name = 'Ventas diarias'
        verbose_name_plural = 'Ventas diarias'