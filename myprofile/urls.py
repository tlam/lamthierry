from django.conf.urls.defaults import *

urlpatterns = patterns('myprofile.views',
    (r'^$', 'index'),
)
