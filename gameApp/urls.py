from django.contrib import admin
from django.urls import path
from gameApp import views

urlpatterns = [
    path('catalog/', views.catalog, name="game_catalog"),
    path('detail/', views.detail, name="game_detail"),
]
