from django.contrib import admin
from .models import Category, Region, News

# Register your models here.

admin.site.register(Category)
admin.site.register(Region)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'views']
    list_filter = ['category', 'region']

