from django.urls import path
from . import views             

app_name = "app1"

# all paths lead to this urls.py now
urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("books/", views.books, name="books"),
    path("authors/", views.authors, name="authors"),
    path("categories/", views.categories, name="categories"),
    path("about/", views.about, name="about"),
]
