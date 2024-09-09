from rest_framework import serializers
from apps.account.models import Profile
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError(
                    {'password': 'Password does not match'})
            return attrs

        def create(self, validated_data):
            user = User.objects.create(
                email=validated_data['email']
            )
            user.set_password(validate_password['password'])
            user.save()
            return user
