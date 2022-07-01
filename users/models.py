from django.db import models
from django.contrib.auth.models import User

class User_profile(models,Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=20)