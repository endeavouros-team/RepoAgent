from django.db import models

# Create your models here.
from django.db import models


class Mirror(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=34)
    sponsor_url = models.CharField(max_length=64, blank=True)

