from django.shortcuts import render_to_response
from myprofile.models import Skill
import django, datetime

def index(request):
    skills = Skill.all()
    django_ver = django.get_version()
    return render_to_response('index.html', {'django_ver': django_ver, 'skills': skills})
