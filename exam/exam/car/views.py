from django.shortcuts import render, redirect

from exam.car.forms import CreateCarForm, EditCarForm, DeleteCarForm
from exam.car.models import Car
from exam.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


# Create your views here.
def create_car(request):
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            user_profile = get_profile()

            car.owner = user_profile
            car.save()

            return redirect('catalogue')
    else:
        form = CreateCarForm()

    return render(request, 'car/car-create.html', {'form': form})


def catalogue(request):
    cars = Car.objects.all()
    total_cars = cars.count()

    return render(request, 'car/catalogue.html', {'cars': cars, 'total_cars': total_cars})


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'car/car-details.html', {'car': car})


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)

    return render(request, 'car/car-edit.html', {'form': form, 'car': car})


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(instance=car)
    return render(request, 'car/car-delete.html', {'form': form, 'car': car})
