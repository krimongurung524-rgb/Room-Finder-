from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from .forms import RoomForm, RoomSearchForm


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


def my_static_page(request):
    return render(request, 'my_static_page.html')

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


def room_search(request):
    form = RoomSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        location = form.cleaned_data.get('location')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        
        results = Room.objects.all()

        if location:
            results = results.filter(location__icontains=location)
        if min_price:
            results = results.filter(price__gte=min_price)
        if max_price:
            results = results.filter(price__lte=max_price)

    context = {
        'form': form,
        'results': results
    }
    return render(request, 'core/room_search.html', context)