from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

#urls that start with musicworld and admin
#url admin is linked to page to manage at backend
#url musicworld and revelant urls linked to show page
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite5.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^musicworld/', include('musicworld.urls', namespace="musicworld")),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH, 'show_indexes':True}),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
