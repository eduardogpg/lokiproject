from django.contrib import admin

from django.urls import path
from django.urls import include

from .views import index
from .views import login
from .views import register
from .views import logout

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('legrappe/admin/admin', admin.site.urls),
    path('', index, name='index'),

    path('login/', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),

    path('wallets/', include('wallets.urls')),
    path('tokens/', include('tokens.urls')),
    path('retrieves/', include('retrieves.urls')),
    path('transactions/', include('transactions.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

