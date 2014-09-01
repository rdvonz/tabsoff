from django.db import models

class Artist(models.Model):
    '''
    Music artist model.
    '''

    artist_name = models.CharField(max_length=50)

class Album(models.Model):
    '''
    Artists may have many different albums.
    '''

    artist = models.ForeignKey(Artist)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

class Song(models.Model):

    models.ForeignKey(Album)
    artist = models.ForeignKey(Artist)
    track_title = models.CharField(max_length=100)
    track_number = models.IntegerField()

