from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import View, ListView
from soc_members.models import Member

# from articles.models import Article

# def home_view(request):
#     return render(request, 'index.html')

class MemberListView(ListView):
    model = Member
    template_name = 'index.html'
    context_object_name = 'members'
    
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context