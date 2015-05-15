from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView
from annet.settings import MEDIA_ROOT, STATIC_URL

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^admin', include(admin.site.urls)),
                       url(r'^login', "AnnetBox.views.login"),
                       url(r'^services', "AnnetBox.views.services"),
                       url(r'^logout', "AnnetBox.views.logout"),
                       url(r'^signup', "AnnetBox.views.signup"),
                       url(r'^portfolio', "AnnetBox.views.portfolio"),
                       url(r'^contacts', "AnnetBox.views.contacts"),
                       url(r'^about', "AnnetBox.views.about"),
                       url(r'^stats', "AnnetBox.views.stats"),
                       url(r'^tickets', "AnnetBox.views.tickets"),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                           'document_root': MEDIA_ROOT,
                       }),
                       (r'^favicon\.ico$', RedirectView.as_view(url='/images/favicon.ico')),
                       (r"", "AnnetBox.views.main", ),

)
