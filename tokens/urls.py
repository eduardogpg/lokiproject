from django.urls import path

from . import views

app_name = 'tokens'

urlpatterns = [
    path('', views.ListTokenView.as_view(), name='list'),
    path('<int:pk>', views.TokenDetailView.as_view(), name='detail'),
    path('<int:pk>/abi', views.abi, name='abi'),
    path('create', views.CreateTokenForm.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateTokenView.as_view(), name='update'),
    path('delete/<int:pk>', views.TokenDeleteView.as_view(), name='delete'),
]