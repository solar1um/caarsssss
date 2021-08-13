from django.contrib import admin
from cars.models import Brand, Car

admin.site.register(Brand)


@admin.register(Car)
class PostAdmin(admin.ModelAdmin):
    list_display = ['brand', 'volume', 'price', 'release_date', 'color',
                    'transmission', 'rul', 'date_created']



 # brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,
 #                              related_name='ads', blank=True, null=True)
 #    author = models.ForeignKey(Profile, on_delete=models.SET_NULL,
 #                               related_name='author_ads', blank=True, null=True)
 #    descriptions = models.TextField(max_length=400)
 #    volume = models.FloatField()
 #    price = models.PositiveIntegerField(default=0)
 #    image = models.ImageField(upload_to='ads', blank=True, null=True)
 #    release_date = models.DateField()
 #    color = models.CharField(max_length=20)
 #    transmission = models.CharField(choices=gear_box, max_length=20,
 #                                    blank=True, null=True)
 #    rul = models.CharField(choices=rul, max_length=6,
 #                           blank=True, null=True)
 #    date_created = models.DateTimeField(auto_now_add=True)
 #    date_modified = models.DateTimeField(auto_now=True)