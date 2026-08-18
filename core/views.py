from django.shortcuts import render, redirect
from .models import Room


def room_list(request):
    all_rooms = Room.objects.all()
    context = {
        'all_rooms': all_rooms
    }
    return render(request, 'core/room_list.html', context)


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    context = {
        'room': room
    }
    return render(request, 'core/room_detail.html', context)


def room_create(request):
    if request.method == 'POST':
        Room.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            price=request.POST.get('price'),
            slug=request.POST.get('slug'),
        )
        return redirect('room_list')

    return render(request, 'core/room_create.html')