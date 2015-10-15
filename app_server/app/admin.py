from django.contrib import admin
from app.models import AppUser, Air, News, Water


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user')


class AirAdmin(admin.ModelAdmin):
    list_display = ('air_id', 'time')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'news_title')


class WaterAdmin(admin.ModelAdmin):
    list_display = ('water_id', 'time')
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Air, AirAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Water, WaterAdmin)
# Register your models here.
