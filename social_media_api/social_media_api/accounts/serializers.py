# accounts/serializers.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserMiniSerializer(serializers.ModelSerializer):
    """
    Read-only compact representation of a user.
    Good for nested usage (followers lists, etc.).
    """
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "bio", "profile_picture",
            "followers_count", "following_count"
        ]
        read_only_fields = ["id", "email", "followers_count", "following_count"]

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Handles new user registration.
    - Validates unique username and email
    - Hashes password correctly
    - Creates/returns an auth token
    """
    password = serializers.CharField(write_only=True, min_length=8)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "bio", "profile_picture", "token"]

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        if value and User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def create(self, validated_data):
        # pop password so we can hash with set_password
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # issue a token for this user
        token, _ = Token.objects.get_or_create(user=user)
        # attach token to serializer output
        user.token = token.key
        return user

    def to_representation(self, instance):
        """
        Ensure the token appears in the response payload.
        """
        data = super().to_representation(instance)
        # When coming from create(), we set instance.token
        if hasattr(instance, "token"):
            data["token"] = instance.token
        else:
            # Fallback if needed
            token, _ = Token.objects.get_or_create(user=instance)
            data["token"] = token.key
        return data


class LoginSerializer(serializers.Serializer):
    """
    Authenticates a user and returns a token.
    - Accepts username and password
    - If you want email login, add an email field and resolve to username first.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        if not user.is_active:
            raise serializers.ValidationError("This account is disabled.")

        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}


class ProfileSerializer(serializers.ModelSerializer):
    """
    Full read/write profile serializer for the authenticated user.
    - Username and email can be optionally editable; adjust read_only_fields as needed.
    - Followers are read-only here to prevent arbitrary manipulation;
      follow/unfollow should be handled by dedicated endpoints.
    """
    followers = UserMiniSerializer(many=True, read_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "bio", "profile_picture",
            "followers", "followers_count", "following_count"
        ]
        read_only_fields = ["id", "followers", "followers_count", "following_count"]

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()

    def update(self, instance, validated_data):
        """
        Allow updating simple profile fields.
        Password changes should go through a dedicated endpoint.
        """
        # Optional: prevent username/email changes; comment out if you want to allow:
        validated_data.pop("username", None)
        validated_data.pop("email", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
