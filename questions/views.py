from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import RoomForm

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
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after creating a new room

    context = {'form': form}
    return render(request, 'questions/room_form.html', context)

def updateRoom(request, pk):
    room  = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after updating the room

    context = {'form': form}
    return render(request, 'questions/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'questions/delete.html',  {'obj':room} )