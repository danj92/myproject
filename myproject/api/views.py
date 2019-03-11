from django.contrib.auth.models import User
from rest_framework import viewsets
from myproject.api.serializers import UserSerializer, DefaultSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class DefaultViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DefaultSerializer

# class LoginViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)

#     def post(self, request,):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         if username is None or password is None:
#             return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
#         user = authenticate(username=username, password=password)

#         if not user:
#             return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
#         token, _ = Token.objects.get_or_create(user=user)

#         return Response({'token': token.key}, status=HTTP_200_OK)
#         # user = authenticate(username=username, password=password)
#         # if user:
#         #     return Response({"token": user.auth_token.key})
#         # else:
#         #     return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
