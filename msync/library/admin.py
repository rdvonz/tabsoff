from django.contrib import admin
from library.models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'artist', 'album')

admin.site.register(Track, TrackAdmin)
