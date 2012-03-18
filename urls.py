from django.conf.urls.defaults import patterns, include, url
import sciagacz
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'laby.views.home', name='home'),
    # url(r'^laby/', include('laby.foo.urls')),
    url(r'^opis_z_wiki/(?P<title>[^/]*)/$', 'sciagacz.views.sciagnij_opis'),
    url(r'^opis_z_wiki/(?P<nazwa>[^/]*)/obrazek(?P<numer>\d+)/', 'sciagacz.views.sciagnij_obrazek'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
