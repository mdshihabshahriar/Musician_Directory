from django.shortcuts import get_object_or_404, redirect, render
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'directory/musician_list.html', {'musicians': musicians})

def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'directory/musician_detail.html', {'form': form})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'directory/album_detail.html', {'form': form, 'album': album})

def add_musician(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm()
    return render(request, 'directory/musician_form.html', {'form': form})

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm()
    return render(request, 'directory/album_form.html', {'form': form})

def delete_musician(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        musician.delete()
        return redirect('musician_list')
    return render(request, 'directory/delete_confirm.html', {'object': musician, 'type': 'musician'})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect('musician_list')
    return render(request, 'directory/delete_confirm.html', {'object': album, 'type': 'album'})
