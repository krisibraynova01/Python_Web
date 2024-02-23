from django.shortcuts import render, redirect

from musicapp.album.models import Album
from musicapp.profiles.forms import ProfileDeleteForm
from musicapp.profiles.models import Profile


def get_profile():
    return Profile.objects.first()

# Create your views here.
def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    return render(request, 'profiles/profile-details.html', {'profile': profile, 'total_albums': albums_count})

def profile_delete(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            albums.delete()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'profiles/profile-delete.html', context)