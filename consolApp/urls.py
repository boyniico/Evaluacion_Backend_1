from django.contrib import admin
from django.urls import path
from consolApp import views

urlpatterns = [
    path('catalog/', views.catalog, name="consol_catalog"),
    path('detail/', views.detail, name="consol_detail")
]
