"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from soc_main.views import MemberListView
from soc_dash.views import main_dash

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_dash, name='home'),
    path('soc_accounts/', include('soc_accounts.urls'), name='soc_accounts'),
    path('soc_members/', include('soc_members.urls'), name='soc_members'),
    path('soc_beneficiaries/', include('soc_beneficiaries.urls'), name='soc_beneficiaries'),
    path('soc_events/', include('soc_events.urls'), name='soc_events'),
    path('soc_documents/', include('soc_documents.urls'), name='soc_documents'),
    path('soc_committees/', include('soc_committees.urls'), name='soc_committees')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
admin.site.site_header ='Stok2Soc Admin Portal' 
admin.site.index_title ='Manage the Stock2Soc Portal'
