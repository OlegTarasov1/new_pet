from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class IsPrivate(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(private=False)


class NewUser(AbstractUser):
    birth_date = models.DateField(blank = True, null = True)
    # phone_number = models.CharField(blank = True)
    private = models.BooleanField(default = False)


    objects = models.Manager()
    notprivate = IsPrivate()