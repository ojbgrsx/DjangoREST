from rest_framework import serializers
from .models import *


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class SecondMovieSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title count_reviews reviews average_rating'.split()

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(movie=movie),
                                      many=True)
        # serializer = ReviewSerializer(product.reviews.all(), many=True)
        return serializer.data
