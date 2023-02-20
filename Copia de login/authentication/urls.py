from django.contrib import admin
from django.urls import path, include
from homepage import views as menu
from . import views


urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name='signup'),
   path('signin', views.signin, name='signin'),
   path('signout', views.signout, name='signout'),
   path('relatos', menu.StoriesListView.as_view(), name='relatos'),
   path('liricas', menu.LyricListView.as_view(), name='liricas'),
   path('frases', menu.PhrasesListView.as_view(), name='frases'),
   path('media', menu.MediaListView.as_view(), name='media'),
   path('reseñas', menu.OthersListView.as_view(), name='reseñas'),
   path('poesia', menu.PoetryListView.as_view(), name='poesia'),
   path('principal', views.principal, name='principal'),
   path('index', views.index, name='index')

]
