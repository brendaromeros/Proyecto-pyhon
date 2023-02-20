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
				blank=True,
        help_text="Ingrese el contenido del relato")

    genre = models.ManyToManyField(
        Genre,
				blank=True,
        help_text="Seleccione un género para este relato")

    score = models.PositiveSmallIntegerField(
				blank=True,
        help_text="Calificación del relato",
				default=0
    )

    front = models.ImageField(
				blank=True,
        help_text="Ingrese una imagen de portada para el relato")

    files = models.FileField(
				blank=True,
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
				blank=True,
        help_text="Ingrese el contenido de la poesía")

    genre = models.ManyToManyField(
        Genre,
				blank=True,
        help_text="Seleccione un género para esta poesía")

    score = models.PositiveSmallIntegerField(
				blank=True,
				default=0,
        help_text="Calificación de la poesía"
    )

    front = models.ImageField(
				blank=True,
        help_text="Ingrese una imagen de portada para la poesía")

    files = models.FileField(
				blank=True,
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
				blank=True,
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
				blank=True,
        help_text="Ingrese el contenido de la frase")

    genre = models.ManyToManyField(
        Genre,
				blank=True,
        help_text="Seleccione un género para esta frae")

    score = models.PositiveSmallIntegerField(
        help_text="Calificación de la frase",
				blank=True,
				default=0
    )

    front = models.ImageField(
				blank=True,
        help_text="Ingrese una imagen de portada para la frase")

    files = models.FileField(
				blank=True,
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
        help_text="Ingrese el contenido de la lírica",
				blank=True)

    genre = models.ManyToManyField(
        Genre,
				blank=True,
        help_text="Seleccione un género para esta lírica")

    score = models.PositiveSmallIntegerField(
				blank=True,
				default=0,
        help_text="Calificación de la lírica"
    )

    front = models.ImageField(
				blank=True,
        help_text="Ingrese una imagen de portada para la lírica")

    files = models.FileField(
				blank=True,
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


class Other(models.Model):
    """
    Modelo que representa un escrito
    """

    name = models.CharField(max_length=200)

    playlist = models.CharField(max_length=200)

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL, null=True)

    content = models.TextField(
        max_length=10000000000,
				blank=True,
        help_text="Ingrese el contenido del escrito")

    genre = models.ManyToManyField(
        Genre,
				blank=True,
        help_text="Seleccione un género para este escrito")

    score = models.PositiveSmallIntegerField(
				blank=True,
				default=0,
        help_text="Calificación del escrito"
    )

    front = models.ImageField(
				blank=True,
        help_text="Ingrese una imagen de portada para el escrito")

    files = models.FileField(
				blank=True,
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
        auto_now=True,
        help_text="última modificación")

    def __str__(self):
        """
        String que representa al objeto Other
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Other
        """
        return reverse('other-detail', args=[str(self.id)])


class Media(models.Model):
    """
    Modelo que representa contenido multimedia
    """

    name = models.CharField(max_length=200)


    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL, null=True)

    content = models.TextField(
        max_length=10000000000,
				blank=True,
        help_text="Ingrese el contenido del archivo")

    genre = models.ManyToManyField(
        Genre,
				blank=True,
        help_text="Seleccione un género para este archivo")

    score = models.PositiveSmallIntegerField(
				blank=True,
				default=0,
        help_text="Calificación del archivo"
    )

    front = models.ImageField(
				blank=True,
        help_text="Ingrese una imagen de portada para el archivo")

    files = models.FileField(
				blank=True,
        help_text="Suba el archivo en formato pdf"
    )

    last_modified = models.DateField(
        auto_now=True,
        help_text="última modificación")

    def __str__(self):
        """
        String que representa al objeto Media
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Media
        """
        return reverse('media-detail', args=[str(self.id)])


