from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import NewUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Info',
            {
                'fields':(
                    'age','nickname'
                )
            }
        )
    )
admin.site.register(NewUser, CustomUserAdmin)