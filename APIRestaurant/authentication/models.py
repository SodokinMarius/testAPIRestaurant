from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import BaseUserManager



'''class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        username_attr = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{username_attr: username})
'''


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        username = self.normalize_email(username)

        user = self.model(username=username, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(username=username, password=password, **extra_fields)


class User(AbstractUser):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=50)

    objects = CustomUserManager()

    USERNAME_FIELD="username"

    def __str__(self):
        return self.username
    