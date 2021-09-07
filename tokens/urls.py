from django.urls import path

from . import views

app_name = 'tokens'

urlpatterns = [
    path('', views.ListTokenView.as_view(), name='list'),
    path('create', views.CreateTokenForm.as_view(), name='create'),
]