# Create your models here.
from django.db import models


# Create your models here.
class Site(models.Model):
    url = models.URLField(unique=True)
    http_code = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=30, blank=True)
    timeout = models.TimeField(blank=True)

    def __str__(self):
        return self.url
