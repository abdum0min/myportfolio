from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog','created_at']
    list_display_links = ['blog']
    search_fields = ['content']