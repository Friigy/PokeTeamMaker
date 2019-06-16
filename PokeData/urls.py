from django.urls import path

from . import views

app_name = 'PokeData'
urlpatterns = [
    path('', views.index, name='index'),
    path('parse/', views.parsePokeCSV, name='parse'),
]