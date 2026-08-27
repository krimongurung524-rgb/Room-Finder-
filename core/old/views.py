from django.shortcuts import render, redirect, get_object_or_404
from core.models import Room
from core.old.forms import RoomForm



def room_list(request):
    all_rooms = Room.objects.all()
    context = {'all_rooms': all_rooms}
    return render(request, 'core/room_list.html', context)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    context = {'room': room}
    return render(request, 'core/room_detail.html', context)



def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
        

    context = {'form': form}
    return render(request, 'core/room_create.html', context)