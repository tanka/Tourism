from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.utils import timezone
from tinymce.models import HTMLField


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=500, blank=True)
    contact_number = models.CharField(max_length=16, blank=True)
    message = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return str(self.name)


# class QuickContact(models.Model):
#     name = models.CharField(max_length=50, blank=True)
#     email = models.CharField(max_length=500, blank=True)

#     def __str__(self):
#         return str(self.name)


class Image(models.Model):
    desc = models.CharField(max_length=1000, blank=True)
    document = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc


class SmallImage(models.Model):
    desc = models.CharField(max_length=1000, blank=True)
    document = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc


class Post(models.Model):
    #  user = models.ForeignKey('auth.User')
    image = models.ForeignKey(Image, null=True)
    thumb_nail = models.ForeignKey(SmallImage, null=True)
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=255, blank=True)
    # content = models.TextField()
    promote = models.BooleanField(default=True)
    content = HTMLField()
    tags = models.CharField(max_length=255, blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True)
    creation_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):  # publish yerine yayinla idi tr tutorial da
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Header(models.Model):
    #  user = models.ForeignKey('auth.User')
    image = models.ForeignKey(Image, null=True)
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=255, blank=True)
    activate = models.BooleanField(default=False)
    position = models.CharField(max_length=5, null=True)

    published_date = models.DateTimeField(
        blank=True, null=True)
    creation_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):  # publish yerine yayinla idi tr tutorial da
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + " -> is active : " + str(self.activate) + " -> at position : " + str(self.position)


class Portfolio(models.Model):
    #  user = models.ForeignKey('auth.User')
    image = models.ForeignKey(Image, null=True)
    short_desc = models.CharField(max_length=255, blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True)
    creation_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.short_desc


class Gallery(models.Model):
    #  user = models.ForeignKey('auth.User')
    image = models.ForeignKey(Image, null=True)
    thumb_nail = models.ForeignKey(SmallImage, null=True)
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=255, blank=True)
    activate = models.BooleanField(default=False)
    position = models.CharField(max_length=5, null=True)

    published_date = models.DateTimeField(
        blank=True, null=True)
    creation_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):  # publish yerine yayinla idi tr tutorial da
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + " -> is active : " + str(self.activate) + " -> at position : " + str(self.position)

