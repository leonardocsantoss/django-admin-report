from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^base/', include('base.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/admin/'}),
    #URLs of the admin-tools
    url(r'^admin_tools/', include('admin_tools.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #URLs of the report
    (r'^report/', include('report.urls')),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )
