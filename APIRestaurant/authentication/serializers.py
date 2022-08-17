from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from .models import User

from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['name','username','password']
    
    def validate(self,attrs):
        username_exists=User.objects.filter(username=attrs["username"]).exists()

        if username_exists:
            raise ValidationError("Username has already been used")
        return super().validate(attrs)
    
    def create(self,validated_data):
        password=validated_data.pop("password")
        user=super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)
        
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]