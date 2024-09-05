from django.db import models
from django.contrib.auth import get_user_model


class Notes(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'notes')
    title = models.CharField(max_length = 255)
    content = models.TextField()
    file = models.FileField(upload_to = 'uploads/')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)