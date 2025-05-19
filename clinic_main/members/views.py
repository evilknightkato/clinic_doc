from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required   # Декоратор для подтверждения пользователя
from django.views.decorators.http import require_POST

from django.db import IntegrityError
from .forms import CustomUserCreationForm,PatientSignUpForm,StaffSignUpForm
from .models import Patient,Staff
# Create your views here.

def home(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        patient_form = PatientSignUpForm(request.POST)

        print("User form errors:", user_form.errors)  # Отладочная печать
        print("Patient form errors:", patient_form.errors)  # Отладочная печать

        if user_form.is_valid() and patient_form.is_valid():
            try:
                # Сначала сохраняем пользователя
                user = user_form.save()
                # Затем создаем Patient с ссылкой на CustomUser
                Patient.objects.create(user=user,polis_num=patient_form.cleaned_data['polis_num'])
                login(request, user)
                print("Регистрация успешна, перенаправляю...")  # Отладочное сообщение
                return redirect('registration_success')
            except Exception as e:
                print("Ошибка при сохранении: ", str(e))  #Отладочное сообщение
                #user_form.add_error('email', 'Этот email уже занят')
        else:
            print("Формы не валидны ")
    else:
        user_form = CustomUserCreationForm()
        patient_form = PatientSignUpForm()

    return render(request,'register.html',{'user_form': user_form,'patient_form': patient_form})

def registration_success(request):
    return render(request, 'registration/success.html')

#@login_required
#def profile(request):
#    patient = request.user.patient
#    return render(request, 'registration/profile.html', {'patient': patient})

@login_required
def profile(request):
    try:
        # Проверяем, является ли пользователь пациентом
        patient_profile = request.user.patient_profile
        return render(request, 'registration/profile.html', {'profile': patient_profile})
    except Patient.DoesNotExist:
        try:
            # Проверяем, является ли пользователь сотрудником
            staff_profile = request.user.staff_profile
            return render(request, 'profile/staff.html', {'profile': staff_profile})
        except Staff.DoesNotExist:
            # Обычный пользователь без профиля
            return render(request, 'profile/base_user.html', {'user': request.user})

@login_required
def logout_confirm(request):
    """Страница подтверждения выхода"""
    return render(request, 'registration/logout_confirm.html')

@require_POST
@login_required
def custom_logout(request):
    """Обработчик выхода из системы"""
    print("Logout called!")  # Должно появиться в консоли сервера
    #messages.info(request, "Вы успешно вышли из системы")
    logout(request)
    return redirect('home')  # Или 'login', если предпочитаете