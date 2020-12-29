
from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='profile_pic/', blank=True, default='default.png')



    def __str__(self):
        return f'{self.user.username} Profile'

   