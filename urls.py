from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('myprofile.urls', namespace='myprofile'), name='myprofile'),
    url(r'^portfolios/', include('portfolios.urls', namespace='portfolios'), name='portfolios'),
)
