from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    location = models.PointField(
        editable=False,
        blank=True,
        null=True,
        default=None)

    def __str__(self):
        return self.user.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Toilet(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=255)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)

    def __str__(self):
        return self.location, self.latitude, self.longitude
