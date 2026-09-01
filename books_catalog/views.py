from django.shortcuts import render
from django.http import Http404
from utils import load_json_app

def catalog(request):
    books = load_json_app("books.json")
    for book in books:
        book['creator'] = book['author']
    return render(request, 'books/catalog.html', {'books': books})

def book_detail(request, book_id):
    books = load_json_app("books.json")
    for book in books:
        book['creator'] = book['author']

    book = next((item for item in books if item['id'] == book_id), None)
    
    if book is None:
        raise Http404("Book not found")
        
    return render(request, 'books/book_detail.html', {'book': book})