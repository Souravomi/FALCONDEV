from User.views import getByLanguage
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('' , views.Admin_Login , name='Admin_Login'),
   path('Home' , views.Admin_Home , name='Admin_Home'),
   path('Profile' , views.Admin_Profile , name='Admin_Profile'),
   path('UI' , views.Admin_UI , name='Admin_UI'),
   path('getByLanguage/<str:lang>/',views.getByLanguage,name='getBylanguage'),
   path('Updations' , views.Admin_Updations , name='Admin_Updations'),
   path('Services' , views.Admin_Services , name='Admin_Services'),
   path('Task' , views.Admin_Task , name='Admin_Task'),
   path('Logout' , views.Logout , name='Logout'),

   #Reset Passwords

   path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]