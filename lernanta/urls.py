from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/',     include('django.contrib.admindocs.urls')),
    (r'^admin/',         include(admin.site.urls)),
    (r'',                include('drumbeat.urls')),
    (r'',                include('dashboard.urls')),
    (r'',                include('wellknown.urls')),
    (r'',                include('activity.urls')),
    (r'^statuses/',      include('statuses.urls')),
    (r'^groups/',        include('projects.urls')),
    (r'^schools/',       include('schools.urls')),
    (r'^relationships/', include('relationships.urls')),
    (r'^messages/',      include('drumbeatmail.urls')),
    (r'^pubsub/',        include('django_push.subscriber.urls')),
    (r'^richtext/',      include('richtext.urls')),
    (r'^pages/',         include('pages.urls')),
    (r'^search/',        include('search.urls')),
    (r'^chat/',          include('chat.urls')),
    (r'^comments/',      include('replies.urls')),
    (r'^badges/',        include('badges.urls')),
    (r'metrics/',        include('tracker.urls')),
    (r'reviews/',        include('reviews.urls')),
    (r'',                include('users.urls')),
    (r'',                include('api.urls')),
)

media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
urlpatterns += patterns('',
    (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
     {
         'document_root': settings.MEDIA_ROOT,
     }),
)

handler500 = 'drumbeat.views.server_error'
