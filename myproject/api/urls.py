from django.conf.urls import url, include
from rest_framework import routers
from myproject.api.views import UserViewSet, DefaultViewSet

from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'login', DefaultViewSet)

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'auth/', views.obtain_auth_token)
]
