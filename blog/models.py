from django.db import models
from django.contrib import admin


# Create your models here.

class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    list_per_page = 100



admin.site.register(BlogsPost, BlogPostAdmin)
