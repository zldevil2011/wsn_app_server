from django.contrib import admin
from app.models import AppUser


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user')

admin.site.register(AppUser, AppUserAdmin)
# Register your models here.
