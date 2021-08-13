from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cars.forms import CreateAdForm
from cars.models import Brand, Car


def main_page(request):
    brand = Brand.objects.all()
    context = {
        'brand': brand
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

    context = {
        'cars': cars
    }
    return render(request, 'cars/cars.html', context)
