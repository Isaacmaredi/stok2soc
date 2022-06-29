from django.urls import path
from . import views

app_name = 'soc_dash'

urlpatterns = [
    path('dashboard/',views.main_dash, name='dashboard'),
]