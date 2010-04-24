from django.conf.urls.defaults import *

urlpatterns = patterns('portfolios.views',
    url(r'^$', 'index', name='index'),
    url(r'^add/$', 'add', name='add'),
    url(r'^update/(?P<slug>[\w-]+)/$', 'update', name='update'),
)
