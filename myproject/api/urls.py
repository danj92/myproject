from django.conf.urls import url, include
from rest_framework import routers
from myproject.api import views

from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'login', views.LoginViewSet, base_name='login')

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'auth/', ObtainAuthToken.as_view())
]
