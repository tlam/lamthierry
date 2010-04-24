from django import forms
from google.appengine.ext.db import djangoforms

from portfolios.models import Portfolio

'''
class PortfolioForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.CharField(max_length=100)
    url = forms.CharField(max_length=200)
    implementation = forms.CharField(max_length=200)
    accomplishment = forms.CharField(max_length=200)
    completed = forms.DateField()
    source = forms.CharField(max_length=200)
    thumbnail = forms.CharField(max_length=200)
    image = forms.CharField(max_length=200)
'''

class PortfolioForm(djangoforms.ModelForm):
    class Meta:
        model = Portfolio
