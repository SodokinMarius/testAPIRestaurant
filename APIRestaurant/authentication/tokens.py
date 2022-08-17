from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

from APIRestaurant import settings

User=get_user_model()


def create_jwt_pair_for_user(user:User):
    refresh=RefreshToken.for_user(user)
    tokens={"access":str(refresh.access_token),"refresh":str(refresh)}
    settings.CURRENT_USER_ACCESS_TOKEN=tokens
    return tokens