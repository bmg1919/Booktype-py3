# This file is part of Booktype.
# Copyright (c) 2014 Helmy Giacoman <helmy.giacoman@sourcefabric.org>
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

from django.urls import re_path

from booktype.apps.core.views import staticattachment
from .views import (
    InfoPageView, DeleteBookView, EditBookInfoView,
    DraftChapterView, FullView, BookCoverView,
    PublishedBookView, PermissionsView
)

app_name = 'reader'

urlpatterns = [
    re_path(r'^$', PublishedBookView.as_view(), name='published_book'),
    re_path(r'^_info/$', InfoPageView.as_view(), name='infopage'),
    re_path(r'^_info/permissions/$', PermissionsView.as_view(), name='permissions'),
    re_path(r'^_info/cover.jpg$', BookCoverView.as_view(), name='book_cover'),
    re_path(r'^_info/edit/$', EditBookInfoView.as_view(), name='edit_info_book'),
    re_path(r'^_info/delete/$', DeleteBookView.as_view(), name='delete_book'),
    re_path(r'^_full/$', FullView.as_view(), name='full_view'),
    re_path(r'^_full/static/(?P<attachment>.*)$', staticattachment),

    # draft book page
    re_path(r'^_draft/_v/(?P<version>[\w\s\_\d\.\-]+)/(?P<chapter>[\w\s\_\.\-]+)/$',
            DraftChapterView.as_view(), name='draft_chapter_page'),
    re_path(r'^_draft/_v/(?P<version>[\w\s\_\d\.\-]+)/(?P<chapter>[\w\s\_\.\-]+)/static/(?P<attachment>.*)$',
            staticattachment),
    re_path(r'^_draft/_v/(?P<version>[\w\s\_\d\.\-]+)/static/(?P<attachment>.*)$',
            staticattachment, name='draft_attachment'),

    re_path(r'^_draft/_v/(?P<version>[\w\s\_\d\.\-]+)/$', DraftChapterView.as_view(), name='draft_chapter_page'),
    re_path(r'^_draft/(?P<chapter>[\w\s\_\.\-]+)/$', DraftChapterView.as_view(), name='draft_chapter_page'),
    re_path(r'^_draft/(?P<chapter>[\w\s\_\.\-]+)/static/(?P<attachment>.*)$', staticattachment),
    re_path(r'^_draft/static/(?P<attachment>.*)$', staticattachment),
    re_path(r'^_draft/$', DraftChapterView.as_view(), name='draft_chapter_page'),
]
