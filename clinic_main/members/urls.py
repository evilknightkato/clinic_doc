from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name='register'),
    path('registration/success/', views.registration_success, name='registration_success'),
    path('registration/profile/', views.profile, name='profile'),
    path('logout/',views.CustomLogoutView.as_view(),name='logout'),
]