from django.conf.urls import include, url
from django.contrib import admin
from apps import users

urlpatterns = [
    # Examples:
    # url(r'^$', 'plangenius.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include(users.urls)),
]
