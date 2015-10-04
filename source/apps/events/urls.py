from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<event_slug>[\w\-]+)/$', views.event_detail, name='event_detail'),
    url(r'^event/(?P<event_slug>[\w\-]+)/meals/$', views.meal_category, name='meal_category'),
]
