from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Patient,Staff  # Ваша кастомная модель

# Register your models here.
admin.site.register(CustomUser, UserAdmin)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('polis_num',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('position',)