from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('music/', include('music_catalog.urls')),
    path('books/', include('books_catalog.urls')),
]
