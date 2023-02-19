# Create your models here.
from django.db import models
from django.urls import reverse


class Author(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Genre(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(
        max_length=200,
        help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return self.name


class Stories(models.Model):
    """
    Modelo que representa un relato
    """

    name = models.CharField(max_length=200)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL, null=True)
    # 'Author' es un string, en vez de un objeto, porque la clase Author aún no ha sido declarada.

    content = models.TextField(
        max_length=10000000000,
        help_text="Ingrese el contenido del relato")

    genre = models.ManyToManyField(
        Genre,
        help_text="Seleccione un género para este relato")

    score = models.PositiveSmallIntegerField(
        help_text="Calificación del relato"
    )

    front = models.ImageField(
        help_text="Ingrese una imagen de portada para el relato")

    files = models.FileField(
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
        auto_now=True,
        help_text="última modificación")

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('storie-detail', args=[str(self.id)])


class Poetry(models.Model):
    """
    Modelo que representa una poesía
    """

    name = models.CharField(max_length=200)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL, null=True)

    content = models.TextField(
        max_length=10000000000,
        help_text="Ingrese el contenido de la poesía")

    genre = models.ManyToManyField(
        Genre,
        help_text="Seleccione un género para esta poesía")

    score = models.PositiveSmallIntegerField(
        help_text="Calificación de la poesía"
    )

    front = models.ImageField(
        help_text="Ingrese una imagen de portada para la poesía")

    files = models.FileField(
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
        auto_now=True,
        help_text="última modificación")

    def __str__(self):
        """
        String que representa al objeto Poetry
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de poetry
        """
        return reverse('poetry-detail', args=[str(self.id)])


class Phrases(models.Model):
    """
    Modelo que representa una Frase
    """

    name = models.CharField(max_length=200)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL, null=True)

    content = models.TextField(
        max_length=10000000000,
        help_text="Ingrese el contenido de la frase")

    genre = models.ManyToManyField(
        Genre,
        help_text="Seleccione un género para esta frae")

    score = models.PositiveSmallIntegerField(
        help_text="Calificación de la frase"
    )

    front = models.ImageField(
        help_text="Ingrese una imagen de portada para la frase")

    files = models.FileField(
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
        auto_now=True,
        help_text="última modificación")

    def __str__(self):
        """
        String que representa al objeto Phrases
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de phrases
        """
        return reverse('phrases-detail', args=[str(self.id)])


class Lyric(models.Model):
    """
    Modelo que representa una lírica
    """

    name = models.CharField(max_length=200)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL, null=True)

    content = models.TextField(
        max_length=10000000000,
        help_text="Ingrese el contenido de la lírica")

    genre = models.ManyToManyField(
        Genre,
        help_text="Seleccione un género para esta lírica")

    score = models.PositiveSmallIntegerField(
        help_text="Calificación de la lírica"
    )

    front = models.ImageField(
        help_text="Ingrese una imagen de portada para la lírica")

    files = models.FileField(
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
        auto_now=True,
        help_text="última modificación")

    def __str__(self):
        """
        String que representa al objeto Lyric
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Lyric
        """
        return reverse('lyric-detail', args=[str(self.id)])
