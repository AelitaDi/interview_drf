from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver

from base.models import LowerCaseEmailField, NULLABLE, BaseModel, LowerCaseUsernameField


class User(AbstractUser, BaseModel):
    """User model."""
    username = LowerCaseUsernameField('username', max_length=25, unique=True)
    email = LowerCaseEmailField('email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserProfile(BaseModel):
    """Profile user."""
    user = models.OneToOneField(User, models.CASCADE, related_name='profile', verbose_name='user')
    address = models.TextField('address', **NULLABLE)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    @staticmethod
    @receiver(models.signals.post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and sender == User and kwargs:
            UserProfile.objects.create(user=instance)
