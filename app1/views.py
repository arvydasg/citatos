from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="app1/home.html",
                  context={"quote": Quote.objects.all})
