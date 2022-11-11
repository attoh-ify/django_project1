from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + "_" + self.last_name + "_"


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.today)
    likes = models.CharField(max_length=40)
    artiste_id = models.CharField(max_length=40)

    def __str__(self):
        return self.title + "_( by " + self.Artiste.first_name + "_" + self.Artiste.last_name + ")"


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    song_id = models.CharField(max_length=40)

    def __str__(self):
        return self.song_id + " (" + self.Song.Artiste.first_name + "_" + self.Song.Artiste.last_name + "/" + self.Song.title + ")"
