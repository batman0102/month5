from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class UserCreateValidationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=3)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('User already exists!')

class UserLoginValidationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=3)