from django.contrib import admin
from .models import Contact, Image, SmallImage, Portfolio, Post, Header, Gallery
# Register your models here.


admin.site.register(Contact)
# admin.site.register(QuickContact)
admin.site.register(Image)
admin.site.register(SmallImage)
admin.site.register(Portfolio)
admin.site.register(Post)
admin.site.register(Header)
admin.site.register(Gallery)
