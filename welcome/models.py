from django.db import models


# Create your models here.
class Actor(models.Model):
    myID = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=3000)
    profile = models.CharField(max_length=3000)
    jpg = models.CharField(max_length=200)
    short = models.TextField(default='/')

    def __str__(self):
        return f"{self.myID}\n{self.name}\n{self.info}\n{self.profile}\n{self.jpg}"


class Movie(models.Model):
    myID = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    directors = models.CharField(max_length=500)
    authors = models.CharField(max_length=600)
    actorsShort = models.CharField(max_length=5000)
    profile = models.TextField()
    rating = models.CharField(max_length=5)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"{self.myID}\n{self.name}\n{self.image}\n{self.directors}\n{self.profile}\n{self.rating}\n{self.actors}\n{self.comment_set}"


class Comment(models.Model):
    content = models.TextField()
    short = models.TextField(default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"


class Coworker(models.Model):
    myID = models.CharField(max_length=10)
    times = models.IntegerField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.myID}\n{self.times}"
