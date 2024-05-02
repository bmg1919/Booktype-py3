# This file is part of Booktype.
# Copyright (c) 2013 Aleksandar Erkalovic <aleksandar.erkalovic@sourcefabric.org>
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

from django.urls import re_path, path

from .views import (
    EditBookPage, BookHistoryPage, RevisionPage,
    ChapterHistoryPage, CompareChapterRevisions, BookSettingsView,
    DownloadBookHistory, InviteCodes
)
from .views import upload_attachment, upload_cover, cover
from booktype.apps.core.views import staticattachment

app_name = 'edit'

urlpatterns = [
    re_path(r'^_upload/$', upload_attachment, name='upload_attachment'),
    re_path(r'^_upload_cover/$', upload_cover, name='upload_cover'),
    re_path(r'^_cover/(?P<cid>[\w\s\_\d\.\-]+)/(?P<fname>.*)$', cover, name='view_cover'),
    re_path(r'^_edit/static/(?P<attachment>.*)$', staticattachment),

    re_path(r'^_edit/$', EditBookPage.as_view(), name='editor'),
    re_path(r'^_history/$', BookHistoryPage.as_view(), name='history'),
    re_path(r'^_history/download/$', DownloadBookHistory.as_view(), name='download_history'),
    re_path(r'^_history/(?P<chapter>[\w\s\_\.\-]+)/download/$',
            DownloadBookHistory.as_view(), name='download_chapter_history'),

    re_path(r'^_history/(?P<chapter>[\w\s\_\.\-]+)/$',
            ChapterHistoryPage.as_view(), name='chapter_history'),

    re_path(r'^_history/(?P<chapter>[\w\s\_\.\-]+)/compare-revs/(?P<rev_one>\d+)/(?P<rev_two>\d+)/$',
            CompareChapterRevisions.as_view(), name='revisions_compare'),

    re_path(r'^_history/(?P<chapter>[\w\s\_\.\-]+)/rev/(?P<revid>\d+)/$',
            RevisionPage.as_view(), name='chapter_revision'),

    re_path(r'^_history/(?P<chapter>[\w\s\_\.\-]+)/rev/(?P<revid>\d+)/static/(?P<attachment>.*)$',
            staticattachment),

    re_path(r'^_settings/$', BookSettingsView.as_view(), name='settings'),

    re_path(r'^_invite_codes/$', InviteCodes.as_view(), name='invite_codes'),
]
