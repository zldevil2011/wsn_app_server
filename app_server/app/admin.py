from django.contrib import admin
from app.models import AppUser, Air, News


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user')


class AirAdmin(admin.ModelAdmin):
    list_display = ('air_id', 'pm25')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'news_title')

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Air, AirAdmin)
admin.site.register(News, NewsAdmin)
# Register your models here.
