from django.conf.urls import include, patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap

# from cms.sitemaps import CMSSitemap

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from apps.users import views
from apps.events import urls
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'plangenius.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event/', include(urls)),
    url(r'^sign-up/$', views.sign_up, name='sign-up'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]

# import os



if getattr(settings, "LOCAL_SERVE", False):
    urlpatterns = patterns(
        'django.views.static',
        url(
            r"^%s(?P<path>.*)$" % settings.MEDIA_URL.lstrip('/'),
            "serve",
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True,
            }),
    ) + staticfiles_urlpatterns() + urlpatterns