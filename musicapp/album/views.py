from django.shortcuts import render, redirect
from musicapp.album.forms import AlbumForm, EditAlbum, DeleteAlbum
from musicapp.profiles.models import Profile
from musicapp.album.models import Album

def get_profile():
    return Profile.objects.first()

def get_album(pk):
    album = Album.objects.filter(id=pk).get()
    return album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            # Retrieve the user's profile
            profile = get_profile()

            # Associate the new album with the user's profile
            album = form.save(commit=False)
            album.owner = profile
            album.save()

            # Redirect to the home page
            return redirect('index')  # Adjust 'home' to your home template URL
    else:
        form = AlbumForm()

    return render(request, 'album/album-add.html', {'form': form})

def details_album(request,pk):
    album = Album.objects.get(pk=pk)
    context = {'album': album}
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')  # Adjust 'home' to your home template URL
    else:
        form = EditAlbum(instance=album)

    return render(request, 'album/album-edit.html', {'form': form, 'album': album})

def delete_album(request, pk):
    album = get_album(pk)

    if request.method == 'POST':
        album.delete()
        return redirect('index')  # Adjust 'home' to your home template URL

    form = DeleteAlbum(instance=album)
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'album/album-delete.html', context)


