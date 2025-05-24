
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,verbose_name='Email')
    first_name = models.CharField(max_length=100,blank=True,verbose_name='Имя')
    last_name = models.CharField(max_length=100,blank=True,verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100,blank=True,verbose_name='Отчество')
    phone_user = models.CharField(max_length=20,blank=True,verbose_name='Телефон')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @classmethod
    def generate_username(cls):
        """Генерация username в формате userXXXX"""
        max_id = cls.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        return f"user{max_id + 1:04d}"

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,primary_key=True,related_name='patient_profile')
    polis_num = models.CharField(max_length=16,blank=True,verbose_name='Номер полиса')
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,primary_key=True,related_name='staff_profile')
    position = models.CharField(max_length=100,blank=True,verbose_name='Должность')
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

@receiver(pre_save, sender=CustomUser)
def set_auto_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = CustomUser.generate_username()