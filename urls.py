from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

''' patterns default
urlpatterns = patterns('',
    # Example:
    # (r'^meu_blog/', include('meu_blog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
'''

from blog.models import Artigo
from blog.feeds import UltimosArtigos
urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index', {'queryset': Artigo.objects.all(), 'date_field': 'publicacao'}),
    (r'^admin/(.*)', admin.site.root),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': {'ultimos': UltimosArtigos}}),
    (r'^artigo/(?P<slug>[\w_-]+)/$', 'blog.views.artigo'),
    (r'^contato/$', 'views.contato'),
    (r'^comments/', include('django.contrib.comments.urls')),)

#(r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),

# < (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), <== Retirado para  uso do local_settings.py

if settings.LOCAL:
    urlpatterns += patterns('',(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),)

