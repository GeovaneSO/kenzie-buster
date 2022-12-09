from django.urls import path
from . import views

urlpatterns = [
    path("movies/"),
    path("movies/<int:movie_id>/")
]