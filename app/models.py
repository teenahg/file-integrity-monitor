from django.db import models
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()

class File(models.Model):
    name = models.CharField(max_length=350)
    location = models.CharField(max_length=350)
    hash_value = models.CharField(max_length=32)
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager