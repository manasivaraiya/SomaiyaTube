from django.contrib import admin
from website.models import User,NewVideo,Comment


# Register your models here.

admin.site.register(NewVideo)
admin.site.register(Comment)
