from django.db import models


class MoviesOptions(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    MC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=MoviesOptions.choices, default=MoviesOptions.G, null=True)
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies")
