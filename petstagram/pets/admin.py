from django.contrib import admin

from petstagram.pets.models import Pet


@admin.register(Pet)
class PedAdmin(admin.ModelAdmin):
    pass
