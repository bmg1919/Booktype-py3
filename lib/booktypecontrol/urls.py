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

from django.urls import path
from . import views as cc_views

app_name = 'control_center'

urlpatterns = [
    path('', cc_views.ControlCenterView.as_view(), name='frontpage'),
    path('settings/', cc_views.ControlCenterSettings.as_view(), name='settings'),

    path('statistics/', cc_views.StatisticsView.as_view(), name='statistics'),
    path('people/', cc_views.PeopleListView.as_view(), name='people_list'),
    path('people/<username>/info/', cc_views.PersonInfoView.as_view(), name='person_info'),
    path('people/<username>/edit/', cc_views.EditPersonInfo.as_view(), name='person_edit'),
    path('people/<username>/password/', cc_views.PasswordChangeView.as_view(), name='password_change'),

    path('books/<bookid>/rename/', cc_views.BookRenameView.as_view(), name='rename_book'),
    path('groups/<groupid>/delete/', cc_views.DeleteGroupView.as_view(), name='delete_group'),
    path('licenses/<pk>/edit/', cc_views.LicenseEditView.as_view(), name="license_edit"),
    path('licenses/<pk>/delete/', cc_views.DeleteLicenseView.as_view(), name="delete_license"),

    path('roles/<pk>/edit/', cc_views.RoleEditView.as_view(), name="role_edit"),
    path('roles/<pk>/delete/', cc_views.DeleteRoleView.as_view(), name="delete_role"),

    path('book-skeleton/<pk>/edit/', cc_views.BookSkeletonEditView.as_view(), name="book_skeleton_edit"),
    path('book-skeleton/<pk>/delete/', cc_views.DeleteBookSkeletonView.as_view(), name="delete_book_skeleton"),
]
