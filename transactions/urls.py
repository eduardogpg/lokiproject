from django.urls import path

from . import views

app_name = 'transactions'

urlpatterns = [
    path('detail/<int:pk>', views.TransactionDetailView.as_view(), name='detail'),
]