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
   path('poesia', menu.PoetryListView.as_view(), name='poesia'),
   path('principal', views.principal, name='principal'),
   path('index', views.index, name='index')

]
