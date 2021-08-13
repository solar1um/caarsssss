from django import forms
from cars.models import Car, Brand


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand', 'model', 'volume', 'image',
            'release_date', 'transmission', 'color',
            'rul', 'price', 'description',
        ]
        labels = {
            'price': ("Price $")
        }

