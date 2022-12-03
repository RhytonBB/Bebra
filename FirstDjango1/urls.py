"""FirstDjango1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static
items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 4, "name": "Картофель фри" ,"quantity":1},
{"id": 5, "name": "Кепка" ,"quantity":124},
]
urlpatterns = [
path('', views.home),
path('about/', views.about),
path(f"items/{items[0].get('id')}", views.item1),
path(f"items/{items[1].get('id')}", views.item2),
path(f"items/{items[2].get('id')}", views.item3),
path(f"items/{items[3].get('id')}", views.item4),
path(f"items/{items[4].get('id')}", views.item5),
path('items', views.item_list),
path('test/',views.test)

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
