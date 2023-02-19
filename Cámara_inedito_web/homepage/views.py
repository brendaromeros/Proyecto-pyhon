from django.shortcuts import render
from .models import Phrases, Lyric, Stories, Poetry
from .models import Author, Genre


# Create your views here.

def home(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_stories=Stories.objects.all().count()
    num_authors=Author.objects.count()
    num_lyricss = Lyrics.objects.all().count()
    num_phrasess = Phrases.objects.all().count()
    num_poetrys = Poetry.objects.all().count()
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
         'homepage/home.html',
        context={
            'num_stories':num_stories,
            'num_authors':num_authors,
            'num_lyricss':num_lyricss,
            'num_phrasess':num_phrasess,
            'num_poetrys':num_poetrys}

    )

