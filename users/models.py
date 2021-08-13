from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    phone = models.CharField(max_length=20)

