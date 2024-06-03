
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from users.serializers import UserCreateValidationSerializer, UserLoginValidationSerializer
from rest_framework.authtoken.models import Token
from users.models import ActivationCode

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            is_active=False
        )
        verification_code = 123456
        ActivationCode.objects.create(user=user, verification_code=verification_code)

        return Response({'user_id': user.id, 'verification_code': verification_code}, status=status.HTTP_201_CREATED)


class ConfirmRegistrationAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        verification_code = request.data.get('verification_code')

        try:
            user = User.objects.get(username=username)
            activation_code = ActivationCode.objects.get(user=user, verification_code=verification_code)

            if activation_code.is_verified:
                return Response({'error': 'User is already verified.'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_active = True
            user.save()
            activation_code.is_verified = True
            activation_code.save()

            return Response({'detail': 'Registration confirmed.'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except ActivationCode.DoesNotExist:
            return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserLoginValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})

        return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'User credentials are wrong!'})



