from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    user_id = models.CharField(max_length=255)
    time_crerate = models.DateTimeField(auto_now_add=True)
    last_time_update = models.DateTimeField(auto_now=True)
