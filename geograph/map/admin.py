from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.PeopleOfVaak)
class VaakAdmin(admin.ModelAdmin):
    list_display = ["name"]