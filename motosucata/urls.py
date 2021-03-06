from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    #(r'^pages/', include('django.contrib.flatpages.urls')),
    
    url(r'^$', 'products.views.index', name='home'),
    url(r'^contact/?$', 'products.views.contact'),
    url(r'^(?P<slug>[\w_-]+)$', 'products.views.details'),
    url(r'^q/(?P<column>(type)?)/?(?P<text>[\w -]{0,100})$', 'products.views.search'),
)

try:
    urlpatterns += patterns('', (r'^flexselect/', include('flexselect.urls')), )
except ImportError:
    urlpatterns += patterns('flexselect.views', (r'field_changed', 'field_changed'), )

if settings.LOCAL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)