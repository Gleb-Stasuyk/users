from django.contrib.auth import get_user_model
from rest_framework import  serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer): # pylint: disable=too-few-public-methods

    password = serializers.RegexField(
        "^(?=.*[A-Z])(?=.*\d).{8,}$", max_length=128,
        allow_blank=False, trim_whitespace=True,
        write_only=True, required=True
        )
    username = serializers.CharField(
        required=True, max_length=150,
        allow_blank=False, trim_whitespace=True
        )
    is_active = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name',
            'is_active', 'last_login', 'is_superuser', 'password'
            ]
        read_only_fields = ['id', 'last_login', 'is_superuser']
