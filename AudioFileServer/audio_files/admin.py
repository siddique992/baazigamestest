from django.contrib import admin
from .models import Song, Podcast, AudioBook

@admin.register(Song, Podcast, AudioBook)
class AppAdmin(admin.ModelAdmin):
    pass
