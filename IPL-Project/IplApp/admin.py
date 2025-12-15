from django.contrib import admin
from .models import Franchise, Player, Profile, Stadium

# Register your models here.
admin.site.register(Franchise)
admin.site.register(Player)
admin.site.register(Stadium)
admin.site.register(Profile)