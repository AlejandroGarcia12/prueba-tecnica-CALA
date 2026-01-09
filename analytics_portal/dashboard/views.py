from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth

from dashboard.models import DailySales


def portal_analitico(request):
    """ endpoint con datos de prueba """
    datos = [
        {"date": "2024-08-01", "client": "RetailCo", "metric": "Visitas", "value": "1240"},
        {"date": "2024-08-02", "client": "SaaSify", "metric": "Conversion", "value": "4.1%"},
        {"date": "2024-08-03", "client": "FintechPro", "metric": "Ingresos", "value": "$14,200"},
        {"date": "2024-08-04", "client": "Educa", "metric": "Visitas", "value": "760"},
    ]
    return render(
        request,
        "dashboard/portal_analitico.html",
        {"titulo": "Portal Analítico", "datos": datos},
    )


def total_sales_by_month(request):
    """ Retorna el queryset con el total de ventas por mes """
    query = (
        DailySales.objects.exclude(date__isnull=True)
        .annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total_sales=Sum("value_sale"))
        .order_by("month")
    )
    return render(
        request,
        "dashboard/total_sales_by_month.html",
        {"titulo": "Total de ventas por mes", "rows": query},
    )


def total_sales_by_client(request):
    """ Retorna el queryset con el total de ventas por cliente """
    query = (
        DailySales.objects.values("client_id")
        .annotate(total_sales=Sum("value_sale"))
        .order_by("client_id")
    )

    return render(
        request,
        "dashboard/total_sales_by_client.html",
        {"titulo": "Total de ventas por cliente", "rows": query},
    )
