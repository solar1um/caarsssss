from django import forms
from cars.models import Car, Brand


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'volume', 'mileage', 'fuel', 'image',
            'release_date', 'transmission', 'power', 'color',
            'rul', 'price', 'description', 'extras'
        ]
        labels = {
            'price': ("Price $"),
            'mileage':("Mileage (km)")
        }


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'volume', 'mileage', 'fuel', 'image',
            'release_date', 'transmission', 'power', 'color',
            'rul', 'price', 'description', 'extras'
        ]
        labels = {
            'price': ("Price $"),
            'mileage': ("Mileage (km)")
        }
