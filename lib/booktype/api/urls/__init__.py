from rest_framework import routers
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

from django.urls import re_path, include, path

from ..account import views as account_views
from ..editor import views as editor_views


schema_view = get_schema_view(title='Booktype API')

router = routers.DefaultRouter()
router.register(r'users', account_views.UserViewSet)
router.register(r'books', editor_views.BookViewSet)
router.register(r'languages', editor_views.LanguageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # swagger
    re_path(r'^$', schema_view),

    # auth login/logout
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('v1/', include('booktype.api.urls.v1', namespace='v1')),
]
