from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=500, blank=True)
    contact_number = models.CharField(max_length=16, blank=True)
    message = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return str(self.name)
