from django.shortcuts import render, redirect

from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(username)
        
        if password == password2:
            
            if User.objects.filter(username = username).exists():
                messages.error(request, 'That user name already exists')
                return redirect('soc_accounts:register')
            else:
                if User.objects.filter(email=email).exists() and  User.objects.exclude(email=''):
                    messages.error(request,'That email is already taken')
                    return redirect('soc_accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('soc_accounts:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('soc_accounts:register')      
    else:
        return render (request,'soc_accounts/register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            context= {
                username:"username"
            }
        
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('soc_accounts:login')
    else:
        return render(request, 'soc_accounts/login.html')

def logout(request):  
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect ('soc_accounts:login')
    
class MyPasswordChangeView(PasswordChangeView):
    template_name = 'soc_accounts/password_change_form.html'
    success_url = reverse_lazy ('soc_accounts:change_password_done')
    
class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'soc_accounts/password_change_done.html'
    