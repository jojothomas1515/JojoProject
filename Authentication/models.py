from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    profile_img = models.ImageField( upload_to=f'./profile/{username}/', null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
