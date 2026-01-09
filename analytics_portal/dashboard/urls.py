from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.portal_analitico, name='portal_analitico'),
    path('total_sales_by_month/', views.total_sales_by_month, name='sales_by_month_table'),
    path('total_sales_by_client/', views.total_sales_by_client, name='sales_by_client_table'),
    path('top5_clients/', views.top5_clients, name='top5_clients_table'),
]