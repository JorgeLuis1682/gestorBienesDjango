from django.db import models, transaction
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields you want to include in your user model
    # For example, you can add a 'bio' field:
    bio = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    # You can also add a profile picture field
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    

    
    