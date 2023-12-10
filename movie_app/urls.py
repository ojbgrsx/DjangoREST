from django.urls import path
from .views import *
urlpatterns = [
    path('directors/', director_list_view, name='director_list_view'),
    path('directors/<int:id>', director_detail_view, name='director_detail_view'),
    path('movies/', movie_list_view, name='movie_list_view'),
    path('movies/reviews/', movie_review_average_and_count, name='movie_review_average_and_count'),
    path('movies/<int:id>', movie_detail_view, name='movie_detail_view'),
    path('reviews/', review_list_view, name='review_list_view'),
    path('reviews/<int:id>', review_detail_view, name='review_detail_view'),

]