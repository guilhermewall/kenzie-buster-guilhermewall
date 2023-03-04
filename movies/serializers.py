from rest_framework import serializers
from .models import Movie, MoviesOptions, MovieOrder
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=MoviesOptions.choices, default=MoviesOptions.G, allow_null=True)
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.SerializerMethodField(read_only=True)

    def get_added_by(self, obj):
        email = obj.user.email
        return email

    def create(self, validated_data: dict) -> Movie:

        user_obj = validated_data.pop("user")
        movie = Movie.objects.create(**validated_data, user=user_obj)

        return movie


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def get_title(self, obj):
        title_movie = obj.movie.title
        return title_movie

    def get_buyed_by(self, obj):
        email = obj.user.email
        return email

    def create(self, validated_data):
        movie_order = MovieOrder.objects.create(**validated_data)

        return movie_order

