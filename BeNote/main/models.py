from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название записки")
    text = models.TextField(blank=True, verbose_name="Текст записки")
    user_id = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    last_time_update = models.DateTimeField(auto_now=True)
