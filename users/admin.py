from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustemUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('profile_image','bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('profile_image','bio')}),
    )

admin.site.register(CustomUser,CustemUserAdmin) 
