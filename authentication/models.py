from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# manager for our custom model 
class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class 
    """

    def create_user(self, email=None, first_name=None, last_name=None, password=None):
        if not email:
            raise ValueError("User must have an Email address")
        if not first_name:
            raise ValueError("User must have a First Name")
        if not last_name:
            raise ValueError("User must have a Last Name")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


# Create your models here.
class CustomUser(AbstractUser):
    # ( -1 Not Started ) (0 - Unconfirmed ) (1 - Partially Confirmed ) ( 2 - Confirmed )
    email = models.EmailField(_('email address'), unique=True)
    premium_status = models.IntegerField(null=False, default=-1)
    username = None
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
