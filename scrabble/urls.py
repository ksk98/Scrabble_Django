from django.urls import path

from scrabble import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.room, name='room'),
]