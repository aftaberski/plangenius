from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^/event/(?P<event_slug>[\w\-]+)/category/(?P<category_slug>[\w\-]+)/$', views.event_category, name='category'),
    url(r'^$', views.index, name='index'),
]
