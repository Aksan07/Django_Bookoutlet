from django.shortcuts import render,get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books=Book.objects.all().order_by("title")
    num_book = books.count()
    avg_rating=books.aggregate(Avg("rating"))
    return render(request,"book_outlet/index.html",{
        "books":books,
        "avg_rating":avg_rating,
        "num_book":num_book,
    })
def book_detail(request,slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "rating":book.title,
        "author":book.author,
        "is_bestselling":book.is_bestselling,
    })
    
