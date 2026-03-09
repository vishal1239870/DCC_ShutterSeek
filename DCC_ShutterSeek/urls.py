"""
URL configuration for DCC_ShutterSeek project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render
import requests

def index(request):
    return render(request,"index.html")


def search_photos(request):
    query = request.GET.get('query', '')
    photos = []
    if query:
        access_key = "pOaGpQzANewm-7ZCLWkkKnSL_qHsnrxymJT-O6uYDoo"
        url = "https://api.unsplash.com/search/photos"
        headers = {
            "Authorization": f"Client-ID {access_key}"
        }
        params = {
            "query": query,
            "page": 1,
            "per_page": 30
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            results = response.json().get('results', [])
            for photo in results:
                author_info = {
                    "name": photo["user"]["name"],
                    "username": photo["user"]["username"],
                    "profile_url": photo["user"]["links"]["html"]
                }
                photos.append({
                    "id": photo["id"],
                    "description": photo.get("description", ""),
                    "alt_description": photo.get("alt_description", ""),
                    "urls": photo["urls"],
                    "author": author_info,
                    "likes": photo["likes"]
                })
    return render(request, 'index.html', {'photos': photos, 'query': query})

def search_photos_pixabay(request):
    query = request.GET.get('query', '')
    photos = []
    if query:
        access_key = "19589380-1240f8aee6f52bac7ca20f4ef"
        url = "https://pixabay.com/api/"
        params = {
            "key": access_key,
            "q": query,
            "image_type": "photo",
            "per_page": 30,
            "page": 1
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get('hits', [])
            for photo in results:
                author_info = {
                    "name": photo["user"],
                    "username": photo["user_id"],
                    "profile_url": f"https://pixabay.com/users/{photo['user']}-{photo['user_id']}/"
                }
                photos.append({
                    "id": photo["id"],
                    "description": photo.get("tags", ""),
                    "alt_description": photo.get("tags", ""),
                    "urls": {
                        "small": photo["webformatURL"],
                        "medium": photo["largeImageURL"],
                        "large": photo["largeImageURL"]
                    },
                    "author": author_info,
                    "likes": photo.get("likes", 0)
                })
    return render(request, 'index.html', {'photos': photos, 'query': query})

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path('search/', search_photos, name='search_photos'),
    path('search-pixabay/', search_photos_pixabay, name='search_photos_pixabay'), 

]
