from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import MinutesForm
from .models import Minutes
# Create your views here.
def minutes_list(request):
    minutes = Minutes.objects.all()
    
    return render(request, 'soc_documents/minutes.html',{'minutes':minutes})


def upload_minutes(request):
    if request.method == 'POST':
        form = MinutesForm(request.POST, request.FILES)
    
        if form.is_valid():
            instance = form.save(commit=False)
            instance.uploaded_by = request.user
            instance.save()
            return redirect('soc_documents:minutes_list')
    else:
        form = MinutesForm()
    
    context ={
        
        'form':form,
    }
    return render(request, 'soc_documents/minutes_form.html',context)


    if form.is_valid():
        
        instance.creator = request.user
        instance.save()

