from django.shortcuts import render

from datetime import datetime, date, timedelta

# Create your views here.

def age(self, birth_date):
    if self.birth_date and self.status == 'Active':
        birth_year = self.birth_date.year
        this_year = datetime.now().year
        member_age = this_year - birth_year
        return member_age
    else:
        return 'N/A'