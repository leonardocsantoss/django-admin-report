from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<report_id>\d+)/$', 'report.views.report', name="report"),
)