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

from django.urls import re_path, path
from booki.editor.views import (
    thumbnail_attachment, view_cover, upload_attachment,
    upload_cover, edit_book, view_books_autocomplete
)
from booktype.apps.core.views import staticattachment


urlpatterns = [
    # utility views
    path('_utils/thumbnail/<attachment>', thumbnail_attachment, name='thumbnail_attachment'),
    path('_cover/<cid>/<fname>', view_cover, name='view_cover'),

    # upload
    path('_upload/',  upload_attachment, name='upload_attachment'),
    path('_upload_cover/',  upload_cover, name='upload_cover'),

    # book editing
    path('_edit/', edit_book, name='edit_book'),
    path('_edit/static/<attachment>', staticattachment),
    path('_edit/book-list.json', view_books_autocomplete),
]
