from django.urls import path

from .views import (home_view,CustomLoginView,register_view,profile_redirect_view,patient_profile_view,
                    staff_dashboard_view,logout_view,custom_logout,registration_success)
                    #, profile_redirect_view, staff_dashboard_view, patient_profile_view, logout_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_redirect_view, name='profile_redirect'),  # Роутер
    path('staff/dashboard/', staff_dashboard_view, name='staff_dashboard'),
    path('patient/profile/', patient_profile_view, name='patient_profile'),
    path('logout/confirm/', logout_view, name='logout_confirm'),
    path('logout/', custom_logout, name='logout'),
    #
    # # Страницы успеха
    path('registration/success/', registration_success, name='registration_success'),
]