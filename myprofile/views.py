import datetime

import django
from django.shortcuts import render_to_response
from google.appengine.ext import db

from myprofile.models import Skill

def index(request):
    active_date = datetime.date(2005, 2, 7)
    query = db.Query(Skill)
    query.filter('active =', True)
    active_skills = query.fetch(10)

    query = db.Query(Skill)
    query.filter('active =', False)
    inactive_skills = query.fetch(10)

    django_ver = django.get_version()
    return render_to_response('index.html', {
        'django_ver': django_ver, 
        'active_skills': active_skills,
        'inactive_skills': inactive_skills,
        'active_date': active_date})
