import os
import fnmatch

from django.core.management.base import BaseCommand, CommandError
from library.models import Track
from mutagen.mp3 import EasyMP3 as MP3

class Command(BaseCommand):
    args = 'path to folder containing music files'
    help = 'Adds files to database'

    def handle(self, *args, **options):

        #thanks to  http://rosettacode.org/wiki/Walk_a_directory/Recursively#Python

        for music_path in args:
            for root, dirs, files in os.walk(music_path):
                for filename in fnmatch.filter(files, '*.mp3'):
                    music_tags = MP3(os.path.join(root, filename))
                    try:
                        track = Track(
                        title=music_tags['title'][0],
                        number = int(music_tags['tracknumber'][0].split('/')[0]),
                        artist = music_tags['artist'][0],
                        album = music_tags['album'][0],
                    )
                    except KeyError:
                        raise CommandError('Track %s Is missing Tag Information!' % filename)
                    track.save()


