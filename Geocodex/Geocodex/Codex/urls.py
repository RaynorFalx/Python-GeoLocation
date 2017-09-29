from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/$', include(admin.site.urls), name='admin'),
    url(r'^index/$', list_target, name='list_target'),
    url(r'^details/(?P<target_id>[0-9]+)/$', target_details , name='details'),
]
