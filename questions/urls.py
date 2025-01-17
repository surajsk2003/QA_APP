from django.urls import path
from . import views 
#this is an for importing an views files becuase it in same app.

urlpatterns = [
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room', views.createRoom,name="create-room"),
]

