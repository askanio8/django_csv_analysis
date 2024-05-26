from typing import ClassVar, List, Optional, Type

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: Optional[str] = None, **extra_fields) -> Type["CustomUser"]:
        if not email:
            msg = "The Email field must be set"
            raise ValueError(msg)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: Optional[str] = None, **extra_fields) -> Type["CustomUser"]:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[List[str]] = []

    def __str__(self) -> str:
        return self.email


class UploadRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)
    filename = models.CharField(max_length=255)
    folder_address = models.CharField(max_length=255)
    file_address = models.FileField(upload_to="history/")

    def __str__(self) -> str:
        return self.filename
