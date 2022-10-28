from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models


class Artiste(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField()
    date_released = models.CharField()
    likes = models.CharField()
    artiste_id = models.CharField()


class Lyric(models.Model):
    content = models.CharField()
    song_id = models.CharField()
