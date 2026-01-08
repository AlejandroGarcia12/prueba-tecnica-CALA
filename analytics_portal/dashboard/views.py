from django.shortcuts import render


def portal_analitico(request):
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
