import django_filters
from .models import Member, Beneficiary

class MemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['user', 'status']
        
