import pytest

from rest_framework import status
from rest_framework.test import APIClient, DjangoClient

from django.urls import reverse


@pytest.mark.django_db
class TestChapterListCreateAnonymous(object):
    def test_list_chapters_no_book(self):
        response = DjangoClient().get(
            reverse("v1:editor_chapter_list_create_api", kwargs={'pk': 1})
        )

        assert response.status_code is status.HTTP_403_FORBIDDEN

    def test_create_chapter_no_book(self):
        response = APIClient().post(
            reverse("v1:editor_chapter_list_create_api", kwargs={'pk': 1})
        )

        assert response.status_code is status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize('books', [('First Book',)], indirect=True)
    def test_list_chapters(self, books):
        response = APIClient().get(
            reverse("v1:editor_chapter_list_create_api", kwargs={'pk': books[0].id})
        )

        assert response.status_code is status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize('books', [('First Book',)], indirect=True)
    def test_create_chapter(self, books):
        response = APIClient().post(
            reverse("v1:editor_chapter_list_create_api", kwargs={'pk': books[0].id})
        )

        assert response.status_code is status.HTTP_403_FORBIDDEN
