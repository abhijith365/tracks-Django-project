from django.db import models

# Create your models here.


class Tracks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
