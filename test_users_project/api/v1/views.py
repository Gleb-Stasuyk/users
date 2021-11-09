from django.contrib.auth import get_user_model
from rest_framework import  serializers, viewsets


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    is_active = serializers.BooleanField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser', 'password']
        read_only_fields = ['id', 'last_login', 'is_superuser']



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

