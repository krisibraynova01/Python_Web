from django import forms
from django.shortcuts import render, redirect

from musicapp.album.models import Album
from musicapp.profiles.models import Profile
from musicapp.web.forms import CreateProfileForm
# Create your views here.

def get_profile():
    return Profile.objects.first()

def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "web/home-no-profile.html", context)
def index(request):
    profile = get_profile()

    if profile is None:
      return create_profile(request)

    context = {
        "albums": Album.objects.all()
    }

    return render(request, 'web/home-with-profile.html',context)