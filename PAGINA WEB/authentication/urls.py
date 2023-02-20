from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name='signup'),
   path('signin', views.signin, name='signin'),
   path('signout', views.signout, name='signout'),
   path('relatos', views.relatos, name='relatos'),
   path('liricas', views.liricas, name='liricas'),
   path('escritos', views.escritos, name='escritos'),
   path('principal', views.principal, name='principal'),
   path('index', views.index, name='index')


]
