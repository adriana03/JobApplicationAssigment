from django.conf.urls import patterns, include, url

from django.conf import settings
from django.utils import importlib

from django.contrib import admin
from django.contrib.auth.views import login, logout

# Autodiscover Admin URL
admin.autodiscover()


# URL patterns
urlpatterns = patterns('',
                       #
                       # DEFAULT_APPS routes
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', login, {'template_name': 'bynder/login.html'}, name='login'),
                       url(r'^logout/$', logout, {'template_name': 'bynder/logout.html'}, name='logout'),
                       )
                       #
                      

# I18n view settings
urlpatterns += patterns('',
                        url(r'^i18n/', include('django.conf.urls.i18n')),

                        )
