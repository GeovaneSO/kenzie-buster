from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
import ipdb


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="email already registered."
            )
        ]
    )
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        is_employee = validated_data.pop("is_employee")
        if is_employee:
            superuser = User.objects.create_superuser(
                **validated_data, is_employee=is_employee
            )
            return superuser
        user = User.objects.create_user(**validated_data, is_employee=is_employee)
        return user
