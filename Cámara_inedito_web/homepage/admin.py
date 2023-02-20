
from django.contrib import admin
from .models import Phrases, Lyric, Stories, Poetry
from .models import Author, Genre, Other, Media

admin.site.register(Phrases)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Stories)
admin.site.register(Lyric)
admin.site.register(Poetry)
admin.site.register(Other)
admin.site.register(Media)
