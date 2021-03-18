from rest_framework import serializers, status
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from djoser.conf import settings
from company.models import Company, Employee, EmployeeClass, MailingAddress, BillingAddress
from .models import ContactUs
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email",)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        user = self.context["request"].user or self.user
        # why assert? There are ValidationError / fail everywhere
        assert user is not None

        try:
            validate_password(attrs["new_password"], user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)})
        return super().validate(attrs)


class PasswordRetypeSerializer(PasswordSerializer):
    confirm_password = serializers.CharField(style={"input_type": "password"})

    default_error_messages = {
        "password_mismatch":
            settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs["new_password"] == attrs["confirm_password"]:
            return attrs
        else:
            self.fail("password_mismatch")


class CurrentPasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"})

    default_error_messages = {
        "invalid_password": settings.CONSTANTS.messages.INVALID_PASSWORD_ERROR
    }

    def validate_current_password(self, value):
        is_password_valid = self.context["request"].user.check_password(value)
        if is_password_valid:
            return value
        else:
            self.fail("invalid_password")


class SetPasswordSerializer(PasswordSerializer, CurrentPasswordSerializer):
    pass


class SetPasswordRetypeSerializer(
        PasswordRetypeSerializer,
        CurrentPasswordSerializer):
    pass


