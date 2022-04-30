from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only':True}
        }
        
    def create(self, validated_data:dict):
        user = User(
            username=validated_data.get('username', None),
            email=validated_data.get('email', None)
        )
        password = validated_data.get('password', None)
        if password:
            user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    