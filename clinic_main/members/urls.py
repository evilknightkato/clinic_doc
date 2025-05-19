from django.contrib.auth.views import LogoutView

from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('register/',views.register,name='register'),
    path('registration/success/', views.registration_success, name='registration_success'),
    path('registration/profile/', views.profile, name='profile'),
    #path('registration/logout/',views.logout_page,name='logout'),
    #path('registration/logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('logout/confirm/', views.logout_confirm, name='logout_confirm'),
    path('logout/', views.custom_logout, name='logout'),

]