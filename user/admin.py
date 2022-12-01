from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name',
                    'email',  'age', 'is_staff', ]
    ordering = ['-is_staff','username']

admin.site.register(CustomUser, CustomerUserAdmin, )
