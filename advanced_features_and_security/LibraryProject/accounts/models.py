from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# --------------------------
# Custom User Manager
# --------------------------
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


# --------------------------
# Custom User Model
# --------------------------
class CustomUser(AbstractUser):
    username = None  # disable username
    email = models.EmailField(unique=True)

    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profiles/", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # no username required

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view article"),
            ("can_create", "Can create article"),
            ("can_edit", "Can edit article"),
            ("can_delete", "Can delete article"),
        ]

    def __str__(self):
        return self.title

