from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # mobile_number = models.CharField(
    #     validators=[phone_regex], max_length=15, blank=True)
    # phone_number = models.CharField(
    #     validators=[phone_regex], max_length=15, blank=True)  # validators should be a list

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Tour(models.Model):
    bookedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    tourName = models.CharField(max_length=30, blank=True)
    dateOfArrival = models.DateField(null=True, blank=True)
    noOfPeople = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # mobile_number = models.CharField(
    #     validators=[phone_regex], max_length=15, blank=True)
    # phone_number = models.CharField(
    #     validators=[phone_regex], max_length=15, blank=True)  # validators should be a list

    def __str__(self):
        return str(self.tourName)


class Guest(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    passport = models.CharField(max_length=30, blank=False)
    dateOfArrival = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)
    sex = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=30, blank=True)
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # mobile_number = models.CharField(
    #     validators=[phone_regex], max_length=15, blank=True)
    # phone_number = models.CharField(
    #     validators=[phone_regex], max_length=15, blank=True)  # validators should be a list

    def __str__(self):
        return str(self.name)
