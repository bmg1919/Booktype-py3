from django.urls import re_path

import booktype.urls

from django.contrib import admin
admin.autodiscover()

# Register additional URls
urlpatterns = [
    # Django Admin interface is disabled by default. If you want it
    # enabled you will have to uncomment couple of lines here.
    # re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # re_path(r'^admin/', admin.site.urls),
] + booktype.urls.urlpatterns
