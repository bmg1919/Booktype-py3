# This file is part of Booktype.
# Copyright (c) 2012 Aleksandar Erkalovic <aleksandar.erkalovic@sourcefabric.org>
#
# Booktype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Booktype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Booktype.  If not, see <http://www.gnu.org/licenses/>.

from django.views import static
from django.conf import settings
from django.urls import re_path, include, path
from django.views.generic.base import TemplateView
from booktype.apps.account.views import profilethumbnail

# This is dispatcher for Sputnik connections.
from sputnik.views import dispatcher as sputnik_dispatcher

SPUTNIK_DISPATCHER = (
    (r'^/booktype/$', 'booktype.apps.core.channel'),
    (r'^/chat/(?P<bookid>\d+)/$', 'booki.channels.chat'),
    (r'^/booktype/book/(?P<bookid>\d+)/(?P<version>[\w\d\.\-.]+)/$', 'booktype.apps.edit.channel')
)

urlpatterns = [
    # internationalization
    path('_i18n/', include('django.conf.urls.i18n')),

    # front page
    # re_path(r'', include('booktype.apps.portal.urls', namespace="portal")),
    path('', include('booktype.apps.portal.urls', namespace="portal")),

    # accounts
    # re_path(r'^accounts/', include('booktype.apps.account.urls', namespace="accounts")),
    path('accounts/', include('booktype.apps.account.urls', namespace="accounts")),

    # booktype control center
    path('_control/', include('booktypecontrol.urls', namespace="control_center")),

    # convert
    # TODO: Add namespace
    path('_convert/', include('booktype.apps.convert.urls')),

    path('data/<path:path>', static.serve, {'document_root': settings.DATA_ROOT, 'show_indexes': True}),

    # misc
    # TODO: replace with new apps
    path('_utils/profilethumb/<profileid>/thumbnail.jpg', profilethumbnail, name='view_profilethumbnail'),

    # sputnik dispatcher
    re_path(r'^_sputnik/$', sputnik_dispatcher, {"map": SPUTNIK_DISPATCHER}, name='sputnik_dispatcher'),

    # messaging application
    # TODO: remove this application
    path('messaging/', include('booki.messaging.urls')),

    # importer application
    path('_importer/', include('booktype.apps.importer.urls', namespace='importer')),

    # API urls
    path('_api/', include('booktype.api.urls')),
]

urlpatterns += [
    # export
    path('<bookid>/', include('booktype.apps.loadsave.urls', namespace='loadsave')),

    # new editor
    path('<bookid>/', include('booktype.apps.edit.urls', namespace='edit')),

    # old editor app
    path('<bookid>/', include('booki.editor.urls')),

    # robots.txt
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # new booktype reader app
    path('<bookid>/', include('booktype.apps.reader.urls', namespace='reader')),
]
