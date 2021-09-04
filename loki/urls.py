from django.contrib import admin

from django.urls import path
from django.urls import include

from .views import index
from .views import login
from .views import register
from .views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('login/', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),

    path('wallets/', include('wallets.urls')),
]

