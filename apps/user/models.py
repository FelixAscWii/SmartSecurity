from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=40
    )
    email = models.EmailField(
        max_length=254, 
        unique=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    REQUIRED_FIELDS = ['username']

    class Meta: 
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username