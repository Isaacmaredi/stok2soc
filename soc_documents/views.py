from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

# Create your views here.
from django.shortcuts import render, redirect
from .forms import MinutesForm, PolicyForm
from .models import Minutes, Policy

# Minutes views
class MinutesListView(ListView):
    model = Minutes
    context_object_name = 'minutes'
    template_name = 'soc_documents/minutes.html'
    
class MinutesAdminListView(ListView):
    model = Minutes
    context_object_name = 'minutes'
    template_name = 'soc_documents/minutes_admin.html'

class MinutesUpdateView(UpdateView):
    model = Minutes
    form_class = MinutesForm
    template_name = 'soc_documents/minutes_update.html'
    success_url = reverse_lazy('soc_documents:minutes-admin')
    
class MinutesDeleteView(DeleteView):  
    model = Minutes
    success_url = reverse_lazy('soc_documents:minutes-admin')
    

def upload_minutes(request):
    if request.method == 'POST':
        form = MinutesForm(request.POST, request.FILES)
    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('soc_documents:minutes-admin')
    else:
        form = MinutesForm()
    
    context ={
        
        'form':form,
    }
    return render(request, 'soc_documents/minutes_form.html',context)

# End minutes views


# Policy views 
class PolicyListView(ListView):  
    model = Policy
    context_object_name = 'policies'
    template_name = 'soc_documents/policy.html'
    
class PolicyAdminListView(ListView):
    model = Policy
    context_object_name = 'policies'
    template_name = 'soc_documents/policy_admin.html'

class PolicyUpdateView(UpdateView):
    model = Policy
    form_class = PolicyForm
    template_name = 'soc_documents/policy_update.html'
    success_url = reverse_lazy('soc_documents:policy-admin')
    
class PolicyDeleteView(DeleteView):  
    model = Policy
    success_url = reverse_lazy('soc_documents:policy-admin')
    

def upload_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST, request.FILES)
    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('soc_documents:policy-admin')
    else:
        form = PolicyForm()
    
    context ={
        
        'form':form,
    }
    return render(request, 'soc_documents/policy_form.html',context)

# End policy views
