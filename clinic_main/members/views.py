from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required   # Декоратор для подтверждения пользователя

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
                #user = user_form.save(commit=False)
                #user.set_password(user_form.cleaned_data['password1'])
                #user.username = user.email
                #user.save()
                user = user_form.save()
                # Затем создаем Patient с ссылкой на CustomUser
                Patient.objects.create(user=user,polis_num=patient_form.cleaned_data['polis_num'])
                #patient = patient_form.save(commit=False)
                #patient.user_ptr = user  # Связываем с CustomUser
                #patient = Patient(first_name = user.first_name,last_name = user.last_name, middle_name = user.middle_name,phone_user = user.phone_user,email = user.email,polis_num=patient_form.cleaned_data['polis_num'])
                #patient.save()
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