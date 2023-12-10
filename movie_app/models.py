from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def count_movies(self):
        return self.movies.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        return self.reviews.all().count()

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text, 'star': i.star} for i in reviews]

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('star'))['star__avg'] or 0


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)

    def __str__(self):
        return f"Review for {self.movie.title}"
