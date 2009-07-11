from datetime import date, datetime

import django
from django.shortcuts import render_to_response
from google.appengine.ext import db

import feedparser
from myprofile.models import Skill

def index(request):
    active_date = date(2005, 2, 7)
    query = db.Query(Skill)
    query.filter('active =', True)
    active_skills = query.fetch(10)

    query = db.Query(Skill)
    query.filter('active =', False)
    inactive_skills = query.fetch(10)

    return render_to_response('index.html', {
        'active_date': active_date,
        'active_skills': active_skills,
        'entries': _blog_entries(), 
        'inactive_skills': inactive_skills})

def _blog_entries():
    """Restful blog reading"""
    url = 'http://www.blogger.com/feeds/1208992760067698611/posts/default/-/code-snippets'
    d = feedparser.parse(url)
    entries = d['entries']
    format_entries = []

    for entry in entries:
        format_entry = {'date': _tuple_to_datetime(entry.published_parsed), 'link': entry.link, 'title': entry.title}
        format_entries.append(format_entry)

    return format_entries

def _tuple_to_datetime(tuple):
    """
    Converts a tuple of at least 7 in length to a datetime object, otherwise
    returns today's datetime
    """
    if len(tuple) >= 7:
        return datetime(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5], tuple[6])
    else:
        return datetime.today()
