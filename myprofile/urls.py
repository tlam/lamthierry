from django.conf.urls.defaults import *

urlpatterns = patterns('myprofile.views',
    url(r'^$', 'index', name='index'),
)
