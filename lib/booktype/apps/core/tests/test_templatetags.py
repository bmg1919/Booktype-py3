import mock

from django.test import TestCase

from ..templatetags import booktype_tags


class UsernameTest(TestCase):
    def test_anonymous(self):
        user = mock.Mock(username='Booktype')
        # user.is_authenticated.return_value = False
        user.is_authenticated = False

        self.assertEqual(booktype_tags.tag_username(user), "Anonymous")

    def test_no_firstname(self):
        user = mock.Mock(username='booktype', first_name='')
        user.is_authenticated.return_value = True

        self.assertEqual(booktype_tags.tag_username(user), "booktype")

    def test_firstname(self):
        user = mock.Mock(username='booktype', first_name=' Booktype User ')
        user.is_authenticated.return_value = True

        self.assertEqual(booktype_tags.tag_username(user), ' Booktype User ')

    def test_firstname_empty(self):
        user = mock.Mock(username='booktype', first_name=' ')
        user.is_authenticated.return_value = True

        self.assertEqual(booktype_tags.tag_username(user), 'booktype')
