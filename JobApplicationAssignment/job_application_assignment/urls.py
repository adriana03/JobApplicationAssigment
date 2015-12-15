from django.conf.urls import patterns, include, url
from django.conf import settings
from django.utils import importlib
from django.views.generic import TemplateView
from bynder.views import winner_view

from django.contrib import admin
from django.contrib.auth.views import login, logout

# Autodiscover Admin URL
admin.autodiscover()
HOME_PAGE_VIEW = getattr(settings, 'HOME_PAGE_VIEW', TemplateView.as_view(template_name="index.html"))

# URL patterns
urlpatterns = patterns('',
                       #
                       # DEFAULT_APPS routes
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
                       url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
                       url(r'^$', HOME_PAGE_VIEW, name='index'),
                       url(r'^winner/$',winner_view, name='winner'),
                       url(r'', include('bynder.urls', namespace='bynder')),   
                       url(r'^accounts/', include('allauth.urls')),                    )
                       
# I18n view settings
urlpatterns += patterns('',
                        url(r'^i18n/', include('django.conf.urls.i18n')),

                        )
