from rest_framework import mixins, viewsets, status, filters, generics
from rest_framework.decorators import api_view, action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, \
    UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, get_user_model
from django.conf import settingsf
from django.core.mail import send_mail
from django.shortcuts import render,  get_object_or_404
from .models import User
from .serializers import SetPasswordRetypeSerializer, ProfileSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


class TokenObtainPairAndRoleView(TokenObtainPairView):
    serializer_class = TokenObtainPairAndRoleSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = TokenObtainPairAndRoleSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            token = serializer.validated_data
            return Response({"tokens":token}, status=status.HTTP_200_OK)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response({"Invalid Login"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def SettingsView(request):
    data = request.data
    response = {}
    user = User.objects.first()
    request.user = user
    response_status = status.HTTP_200_OK
    if data.get('email', None):
        if data.get('email') != user.email:
            profile_serializer = ProfileSerializer(
                data=data, instance=user)
            if profile_serializer.is_valid():
                profile_serializer.save()
            else:
                response.update(profile_serializer.errors)
                response_status = status.HTTP_400_BAD_REQUEST
    if response_status == status.HTTP_200_OK and \
            data.get('current_password', None) and \
            data.get('new_password', None) and \
            data.get('confirm_password', None):
        print(request.user)
        password_serializer = SetPasswordRetypeSerializer(
            data=data, context={"request": request})
        if password_serializer.is_valid():
            # password_serializer.save()
            user.set_password(data.get('new_password'))
            user.save()
        else:
            response.update(password_serializer.errors)
            response_status = status.HTTP_400_BAD_REQUEST
    return Response(response, status=response_status)

