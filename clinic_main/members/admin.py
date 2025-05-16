from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Patient  # Ваша кастомная модель

# Register your models here.
admin.site.register(CustomUser, UserAdmin)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('polis_num',)