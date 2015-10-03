from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
