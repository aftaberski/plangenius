from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from apps.users import views
from apps.events import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'plangenius.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event/', include(urls)),
    url(r'^sign-up/$', views.sign_up, name='sign-up'),
    url(r'^login/$', views.user_login, name='login'),
]
