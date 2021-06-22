from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
# from django.db.models.signals import post_save

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()

class File(models.Model):
    name = models.CharField(max_length=350)
    location = models.CharField(max_length=350)
    hash_value = models.CharField(max_length=32)
    slug = models.SlugField(max_length=250, unique_for_date='updated')
    publish = models.DateTimeField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.name

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager