from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView, LogoutAPI

router = DefaultRouter()
router.register(r'api/v1/users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^login$', LoginView.as_view(), name="users_login"),
    url(r'^logout$', LogoutView.as_view(), name="users_logout"),

    # API Rest login
    url(r'^api/v1/login', views.obtain_auth_token, name="users_api_login"),
    url(r'^api/v1/logout', LogoutAPI.as_view(), name="users_api_logout"),
    url(r'', include(router.urls))
]