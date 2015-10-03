from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from apps.users import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'plangenius.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sign-up/$', views.sign_up, name='sign-up')
]
