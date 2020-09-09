from django.db import models


# Create your models here.
class Actor(models.Model):
    myID = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=3000)
    profile = models.CharField(max_length=3000)
    jpg = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.myID}\n{self.name}\n{self.info}\n{self.profile}\n{self.jpg}"


class Movie(models.Model):
    myID = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    directors = models.CharField(max_length=500)
    authors = models.CharField(max_length=600)
    actorsShort = models.CharField(max_length=5000)
    profile = models.CharField(max_length=5000)
    rating = models.CharField(max_length=5)
    actors = models.ManyToManyField(Actor)


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
