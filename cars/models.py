from PIL import Image
from django.db import models
import datetime
from users.models import Profile


def year_choices():
    return [(str(r), str(r)) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class Brand(models.Model):
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.title


class Car(models.Model):
    gear_box = (
        ('automatic', 'automatic'),
        ('manual', 'manual'),
        ('CVT', 'CVT'),
        ('SMG', 'SMG')
    )
    rul = (
        ('left', 'left'),
        ('right', 'right')
    )

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,
                              related_name='ads', blank=True, null=True)
    model = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                               related_name='author_ads', blank=True, null=True)
    description = models.TextField(max_length=400)
    volume = models.FloatField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='ads', blank=True, null=True)
    release_date = models.CharField(choices=year_choices(), max_length=4)
    color = models.CharField(max_length=20)
    transmission = models.CharField(choices=gear_box, max_length=20,
                                    blank=True, null=True)
    rul = models.CharField(choices=rul, max_length=6,
                           blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1280 or img.width > 720:
            output_size = (1280, 720)
            img.thumbnail(output_size)
            img.save(self.image.path)
