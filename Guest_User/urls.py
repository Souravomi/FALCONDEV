from django.urls import path
from . import views


urlpatterns = [
   path('', views.Guest_Home , name='Home'),
   path('Contact', views.Contact , name='Contact'),
   path('Message', views.Message , name='Message'),
]