from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
from .models import Book
from .models import Author
from .models import Category

# Create your views here.
def index(request):
    return render(request=request,
                  template_name="app1/index.html",
                  context={"quote": Quote.objects.all})

def books(request):
    return render(request=request,
                  template_name="app1/books.html",
                  context={"book": Book.objects.all})

def authors(request):
    return render(request=request,
                  template_name="app1/authors.html",
                  context={"author": Author.objects.all})

def categories(request):
    return render(request=request,
                  template_name="app1/categories.html",
                  context={"category": Category.objects.all})

def about(request):
    return render(request=request,
                  template_name="app1/about.html",)


