from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.conf import settings
import datetime
import jwt

class Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='auth_token',on_delete=models.CASCADE,)
    access = models.CharField(max_length=512, blank = True)
    refresh = models.CharField(max_length=512, blank = True)

    access_expiration = models.DateTimeField(default = timezone.now() + datetime.timedelta(minutes = settings.JWT['ACCESS_EXPIRATION_TIME']))
    refresh_expiration = models.DateTimeField(default = timezone.now() + datetime.timedelta(days = settings.JWT['REFRESH_EXPIRATION_TIME']))

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.access:
            self.access = self._generate_access_token

        if not self.refresh:
            self.refresh = self._generate_refresh_token

        return super().save(*args, **kwargs)


    @property
    def _generate_access_token(self):
        access_dt = timezone.now() + datetime.timedelta(minutes = settings.JWT['ACCESS_EXPIRATION_TIME'])
        token = jwt.encode({"token_type": "access", f"{settings.JWT['user']}": self.user.id, "exp": access_dt}, settings.SECRET_KEY, algorithm="HS256")
        return token

    @property
    def _generate_refresh_token(self):
        refresh_dt = timezone.now() + datetime.timedelta(minutes = settings.JWT['REFRESH_EXPIRATION_TIME'])
        token = jwt.encode({"token_type": "refresh", f"{settings.JWT['user']}": self.user.id, "exp": refresh_dt}, settings.SECRET_KEY, algorithm="HS256")
        return token


    def __str__(self):
        return f'{self.user}'
