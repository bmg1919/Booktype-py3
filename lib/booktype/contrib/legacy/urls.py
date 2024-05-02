from django.urls import patterns, url, include
from django.views.decorators.csrf import csrf_exempt

from .views import ConvertView, ConvertResourceView


urlpatterns = patterns('',
    re_path(r'^(?P<resource_id>.+)$', ConvertResourceView.as_view(), name='convert_resource'),
    re_path(r'^$', csrf_exempt(ConvertView.as_view()), name='convert'),
)