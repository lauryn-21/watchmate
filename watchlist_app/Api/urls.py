from django.contrib import admin
from watchlist_app import views
from django.urls import path


urlpatterns = [
    path('', views.movie_list,name='movie_list'),
]