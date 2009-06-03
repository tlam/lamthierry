from django.shortcuts import render_to_response
from google.appengine.ext import db
from myprofile.models import Skill
import django, datetime

def index(request):
    skills = Skill.all()
    query = db.Query(Skill)
    query.filter('active =', True)
    active_skills = query.fetch(8)
    django_ver = django.get_version()
    return render_to_response('index.html', {
        'django_ver': django_ver, 
        'skills': skills,
        'active_skills': active_skills})
