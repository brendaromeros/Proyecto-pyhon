from django.shortcuts import render
from .models import Phrases, Lyric, Stories, Poetry
from .models import Author, Other, Media, Genre
from django.views import generic


# Create your views here.

def home(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_stories=Stories.objects.all().count()
    num_authors=Author.objects.count()
    num_lyrics = Lyric.objects.all().count()
    num_phrases = Phrases.objects.all().count()
    num_poetrys = Poetry.objects.all().count()
    num_other = Other.objects.all().count()
    num_media = Media.objects.all().count()

    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
         'homepage/home.html',
        context={
            'num_stories':num_stories,
            'num_authors':num_authors,
            'num_lyrics':num_lyrics,
            'num_phrases':num_phrases,
            'num_poetrys':num_poetrys,
            'num_other':num_other,
            'num_media':num_media
            }

    )

class StoriesListView(generic.ListView):
    model = Stories
    paginate_by = 10

class LyricListView(generic.ListView):
    model = Lyric
    paginate_by = 10

class PoetryListView(generic.ListView):
    model = Poetry
    paginate_by = 10

class MediaListView(generic.ListView):
    model = Media
    paginate_by = 10

class PhrasesListView(generic.ListView):
    model = Phrases
    paginate_by = 10

class OthersListView(generic.ListView):
    model = Other
    paginate_by = 10

class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 10

class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10
