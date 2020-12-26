from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.testpage, name="test"),
    path('thanks/', views.thankspage, name="thanks"),
    path('groups/', include('groups.urls', namespace="groups")),
    path('posts/', include('posts.urls', namespace="posts")),
]
