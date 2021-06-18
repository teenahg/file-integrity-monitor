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

    # def get_absolute_url(self):
    #     return reverse('filemanager:file_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

# class User(AbstractUser):
    # is_organiser = models.BooleanField(default=True)
    # is_agent = models.BooleanField(default=False)

# class Department(models.Model):
#     pass

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, null=True, blank=True)
#     phone = models.CharField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return str(self.first_name)

# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         print('Profile created!')

# post_save.connect(create_profile, sender=User)

# def update_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.Profile.save()
#         print('Profile updated!')

# post_save.connect(update_profile, sender=User)