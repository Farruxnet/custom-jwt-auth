from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.conf import settings
import jwt
import datetime
from jwt import PyJWT

class Token(models.Model):
    access = models.CharField(max_length=300, blank = True)
    refresh = models.CharField(max_length=300, blank = True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='auth_token',on_delete=models.CASCADE,)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.access:
            self.access = self.token()

        return super().save(*args, **kwargs)

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.datetime.now() + datetime.timedelta(days=60)
        token = jwt.encode({"some": "payload"}, "asdas", algorithm="HS256")

        return token


    def __str__(self):
        return self.user
