from django.contrib import admin
from .models import UserProfile, Mebel

class MebelAdmin(admin.ModelAdmin):
    list_filter = ('category',)

admin.site.register(UserProfile)
admin.site.register(Mebel, MebelAdmin)
