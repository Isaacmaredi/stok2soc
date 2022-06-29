from django.urls import path
from . import views

app_name = 'soc_accounts'

urlpatterns = [
    path('register/', views.register, name = 'register'), 
    path('', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]

