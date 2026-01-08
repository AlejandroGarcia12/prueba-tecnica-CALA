from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.portal_analitico, name='portal_analitico'),
]