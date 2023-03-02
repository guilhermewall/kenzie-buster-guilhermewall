from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(
        validators=[UniqueValidator(User.objects.all(), message="email already registered.")]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(User.objects.all(), message="username already taken.")]
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=False)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)


    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        return user
    