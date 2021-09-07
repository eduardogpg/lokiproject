from django.urls import path

from . import views

app_name = 'wallets'

urlpatterns = [
    path('', views.ListWalletView.as_view(), name='list'),
    path('create/', views.CreateWalletView.as_view(), name='create'),
    path('delete/<int:pk>', views.WalletDeleteView.as_view(), name='delete'),
]