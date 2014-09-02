from django.db import models
from mutagen.mp3 import EasyMP3 as MP3
class MixTape(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    album_art = models.ImageField(upload_to='album_art')

    def __unicode__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=100)
    number = models.SmallIntegerField()
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    mix = models.ForeignKey(MixTape)
    song_file = models.FileField(upload_to='songs')



    def __unicode__(self):
        return self.title
