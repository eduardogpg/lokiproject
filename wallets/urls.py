from django.urls import path

from . import views

app_name = 'wallets'

urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('create', views.CreateWalletView.as_view(), name='create'),
    path('delete/<int:pk>', views.WalletDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.WalletUpdateView.as_view(), name='update'),
]