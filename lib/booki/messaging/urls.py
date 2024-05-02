# This file is part of Booktype.
# Copyright (c) 2012  Seravo Oy <tuukka@seravo.fi>
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

from django.urls import path
from booki.messaging.views import view_post, view_follow, view_unfollow, view_tag

urlpatterns = [
    path('post/', view_post, name='messaging_post'),
    path('follow/', view_follow, name='messaging_follow'),
    path('unfollow/', view_unfollow, name='messaging_unfollow'),
    path('tags/', view_tag, None, 'view_tag'),
]
