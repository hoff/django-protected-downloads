from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('registration.urls')),
    # user console, only accessible for superusers
    (r'^console/$', 'playground.castle.views.console'),
    # view files, only accessible for authenticated user
    (r'^view/(?P<filename>.*)/$', 'playground.castle.views.view_file'),
    # serving files, only accessible for authenticated users
    (r'^serve/(?P<filename>.*)/$', 'playground.castle.views.serve_file'),
    # downloading files, only accessible for authenticated users
    (r'^download/(?P<filename>.*)/$', 'playground.castle.views.download_file'),    
    
    (r'^$', 'playground.castle.views.home'),

    # Examples:
    # url(r'^$', 'playground.views.home', name='home'),
    # url(r'^playground/', include('playground.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
