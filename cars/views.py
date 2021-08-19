from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from cars.forms import CreateAdForm, CarUpdateForm
from cars.models import Brand, Car


def main_page(request):
    cars = Car.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'index.html', context)


@login_required
def create_ad(request):
    if request.method == 'POST':
        form = CreateAdForm(request.POST, request.FILES)
        # print('something')
        if form.is_valid():
            # print('3873738')
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
        # else:
            # print(form.errors)
    form = CreateAdForm()
    return render(request, 'cars/create_ad.html',
                  context={
                      'form': form
                  }
                            )


def all_cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'cars': page_obj

    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, pk):
    owner = None
    car = Car.objects.filter(id=pk).first()
    if request.user == car.author:
        owner = True
    context = {
        'car': car,
        'owner': owner
    }
    return render(request, 'cars/car_details.html',
                  context)


@login_required
def user_cars(request):
    cars = Car.objects.filter(author=request.user)

    context = {
        'cars': cars
    }
    return render(request, 'cars/user_cars.html',
                  context)


@login_required
def car_update(request, pk):
    car = Car.objects.filter(id=pk).first
    print('CAR')
    if request.method == 'POST':
        print('REQUEST')
        form = CarUpdateForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            print('VALID')
            form.save()
            return redirect('my-cars')
    form = CarUpdateForm(instance=Car)
    context = {
        'car': car,
        'form': form
    }
    return render(request, 'cars/car_update.html', context)


def search(request):
    query = request.GET.get('q')
    cars = Car.objects.filter(brand__title__icontains=query)
    return render(request, 'cars/search.html',
                  context={'cars': cars})


@login_required
def car_delete(request, pk):
    car = Car.objects.filter(author=request.user)
    car.delete()
    return redirect('cars')
