from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<event_slug>[\w\-]+)/$', views.event_detail, name='event_detail'),
    url(r'^event/(?P<event_slug>[\w\-]+)/meals/$', views.meal_category, name='meal_category'),
    url(r'^event/(?P<event_slug>[\w\-]+)/activities/$', views.activity_category, name='activity_category'),
    url(r'^event/(?P<event_slug>[\w\-]+)/accommodations/$', views.accommodation_category, name='accommodation_category'),
    url(r'^event/(?P<event_slug>[\w\-]+)/add-option/$', views.add_option, name='add_option'),
]