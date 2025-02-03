from django.contrib import admin
from .models import Friendmap

class FriendmapAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Friendmap, FriendmapAdmin)