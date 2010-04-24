from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from google.appengine.api import users

from portfolios.forms import PortfolioForm
from portfolios.models import Portfolio

def index(request):
    portfolios = Portfolio.all().order('-completed')

    data = {
        'test': 'test',
        'portfolios': portfolios,
        'users': users,
    }

    return render_to_response(
        'portfolios/index.html',
        data,
        context_instance=RequestContext(request)
    )

def add(request):
    success = False

    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = PortfolioForm()

    data = {
        'form': form,
        'success': success,
    }

    return render_to_response(
        'portfolios/add.html',
        data,
        context_instance=RequestContext(request)
    )

def update(request, slug):
    portfolio = Portfolio.all().filter('slug =', slug)
    if portfolio.count():
        portfolio = portfolio[0]
    else:
        raise Http404

    success = False

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            entity = form.save(commit=False)
            entity.put()
            success = True
    else:
        form = PortfolioForm(instance=portfolio)

    data = {
        'form': form,
        'portfolio': portfolio,
        'success': success,
    }

    return render_to_response(
        'portfolios/update.html',
        data,
        context_instance=RequestContext(request)
    )
