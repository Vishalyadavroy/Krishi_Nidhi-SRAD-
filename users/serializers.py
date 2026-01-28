from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    phone = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email','phone', 'password', 'name', 'role', 'location', 'language')

    def validate(self, data):
        if not data.get("phone"):
            raise serializers.ValidationError("Phone number is required")
        return data

  
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            # email=validated_data.get("email"),
            # name=validated_data.get("name"),
            # phone=validated_data["phone"],
            # password=validated_data["password"],
            # role=validated_data["role"],
            # language=validated_data["language"],
            # location=validated_data.get("location")
            password = password,
            **validated_data
        )
        return user

    

class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        identifier = data.get("identifier")
        password = data.get("password")

        user = None

        # login via email
        if "@" in identifier:
            user = authenticate(email=identifier, password=password)
        else:
            # login via phone
            try:
                user_obj = User.objects.get(phone=identifier)
                if user_obj.check_password(password):
                    user = user_obj
            except User.DoesNotExist:
                pass

        if not user:
            raise AuthenticationFailed("Invalid credentials")

        if not user.is_active:
            raise AuthenticationFailed("Account disabled")

        data["user"] = user
        return data     
        
     


# users/serializers.py
class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone",
            "role",
            "language",
            "created_at",
        )

