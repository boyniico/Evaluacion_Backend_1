from django.contrib import admin
from django.urls import path
from books_catalog import views

urlpatterns = [
    path('catalog/', views.catalog, name="books_catalog"),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
]
