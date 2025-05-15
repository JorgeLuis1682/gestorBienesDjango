# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser 
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'is_active', 'tipo', 'bio']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Removemos password2 ya que no lo necesitamos
        user = CustomUser.objects.create_user(**validated_data)
        return user
