from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from petstagram.accounts.forms import UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class PetstagramUserAdmin(UserAdmin):
    # to show all thing from model in administration site
    form = UserChangeForm
    add_form = UserCreateForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'gender')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)
