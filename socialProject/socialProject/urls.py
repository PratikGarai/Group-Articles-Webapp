from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document=settings.STATIC_ROOT)
