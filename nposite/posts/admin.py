from django.contrib import admin
from .models import Post


class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'image', 'summary', 'body')


admin.site.register(Post, Postadmin)
