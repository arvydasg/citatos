from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
from .models import Quote

# Create your views here.
def index(request):
    return render(request=request,
                  template_name="app1/index.html",
                  context={"quote": Quote.objects.all})

def books(request):
    return render(request=request,
                  template_name="app1/books.html",
                  context={"quote": Quote.objects.all})
