from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class NewUser(AbstractUser):
    birth_date = models.DateField(blank = True, null = True)
    # phone_number = models.CharField(blank = True)
    private = models.BooleanField(default = False)
