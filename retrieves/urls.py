from django.urls import path

from . import views

app_name = 'retrieves'

urlpatterns = [
    path('wallets', views.wallets, name='wallets'),
    path('dashboard/<int:pk>', views.dashboard, name='dashboard'),
    path('balance/<int:pk>', views.balance, name='balance'),
]