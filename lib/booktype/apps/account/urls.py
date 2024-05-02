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
from django.conf import settings
from django.contrib.auth import views as auth_views

from .views import (
    CreateBookView, UserSettingsPage, DashboardPageView,
    ForgotPasswordView, ForgotPasswordEnterView, SignInView,
    SendInviteView, JoinWithCode)

# this won't be required once we upgrade to django 1.10
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-LOGOUT_REDIRECT_URL
logout_context = {'LOGOUT_REDIRECT_URL': getattr(settings, 'LOGOUT_REDIRECT_URL', None)}

app_name = 'accounts'

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),

    path('signout/', auth_views.LogoutView.as_view(), {
        'template_name': '/account/signout.html',
        'extra_context': logout_context}, name='signout'),

    path('forgot_password/', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('forgot_password/enter/', ForgotPasswordEnterView.as_view(), name='forgotpasswordenter'),
    path('invite/', SendInviteView.as_view(), name='invite'),
    path('join/', JoinWithCode.as_view(), name='join_with_code'),

    path('<username>/', DashboardPageView.as_view(), name='view_profile'),
    path('<username>/_create_book/', CreateBookView.as_view(), name='create_book'),
    path('<username>/_settings/', UserSettingsPage.as_view(), name='user_settings'),
]
