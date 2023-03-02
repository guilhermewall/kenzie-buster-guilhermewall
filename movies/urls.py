from django.urls import path
from .views import MovieView, MovieDatailView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDatailView.as_view()),
]
