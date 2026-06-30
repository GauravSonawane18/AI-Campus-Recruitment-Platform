from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={"input_type": "password"},
    )

    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password",
            "confirm_password",
            "role",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):
        # Remove confirm_password as it is not a model field
        validated_data.pop("confirm_password", None)

        # Extract password
        password = validated_data.pop("password")

        # Normalize email
        validated_data["email"] = validated_data["email"].lower()

        # Create user using Django's built-in UserManager
        return User.objects.create_user(
            password=password,
            **validated_data,
        )


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )