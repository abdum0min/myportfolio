from django.contrib import admin
from .models import Work
# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_filter = ['created_at']
    search_fields =['title','description']
    date_hierarchy = 'created_at'
    ordering = ['created_at']