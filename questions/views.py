from django.shortcuts import render
from .models import Room, Message

def home(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'questions/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()  # Fetch all messages related to the room
    context = {
        'room': room,
        'messages': messages
    }
    return render(request, 'questions/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'questions/room_form.html', context)