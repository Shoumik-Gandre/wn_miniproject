from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('positive_message/', views.positive_message, name='positive_message'),
    path('play_music/', views.play_music, name='play_music'),
]
