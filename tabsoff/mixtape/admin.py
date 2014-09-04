from django.contrib import admin
from mixtape.models import Track, MixTape


class TrackInline(admin.TabularInline):
    model = Track

class MixTapeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
                'fields': ('title', 'created_by', 'album_art', 'favorited_by')
        }),
   )

    inlines = [TrackInline]
    list_display = ('title', 'created_by')


admin.site.register(MixTape, MixTapeAdmin)
