"""projektas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views             # from relative import views

app_name = "app1"               # good to use, listen 14:07 https://www.youtube.com/watch?v=yD0_1DPmfKM&list=PLQVvvaa0QuDe9nqlirjacLkBYdgc2inh3

# all paths lead to this urls.py now
urlpatterns = [
    path("", views.homepage, name="homepage"),
]
