from django.db.models import Sum
from django.shortcuts import render, redirect

from exam.car.models import Car
from exam.profiles.forms import ProfileCreateForm, ProfileEditForm, DeleteProfileForm
from exam.profiles.models import Profile

def get_profile():
    return Profile.objects.first()

def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()

    return render(request, 'profiles/profile-create.html', {'form': form})


def profile_details(request):
    user_profile = Profile.objects.first()

    total_price = Car.objects.filter(owner=user_profile).aggregate(Sum('price'))['price__sum'] or 0

    return render(request, 'profiles/profile-details.html', {'user_profile': user_profile, 'total_price': total_price})

def edit_profile(request):
    user_profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = ProfileEditForm(instance=user_profile)

    return render(request, 'profiles/profile-edit.html', {'form': form})

def delete_profile(request):
    user_profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST)
        if form.is_valid():

            user_profile.cars_profile.all().delete()
            user_profile.delete()
            return redirect('index')
    else:
        form = DeleteProfileForm()

    return render(request, 'profiles/profile-delete.html', {'form': form})