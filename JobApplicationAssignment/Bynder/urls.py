from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^bynder/', include('Bynder.urls')),
    url(r'^admin/', admin.site.urls),
]