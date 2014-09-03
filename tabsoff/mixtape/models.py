from django.contrib.auth.models import User
from django.db import models

class MixTape(models.Model):
    '''
    The mixtape model
    '''
    title = models.CharField(max_length=100)
    album_art = models.ImageField(upload_to='album_art')

    #The created_by field won't be accessible by a user, we find that out based on who's logged in
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Track(models.Model):
    '''
    The track model
    '''
    title = models.CharField(max_length=100)
    number = models.SmallIntegerField()
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    #many to one relationship with the MixTape model
    mixtape = models.ForeignKey(MixTape)
    song_file = models.FileField(upload_to='songs')
    def __unicode__(self):
        return self.title
