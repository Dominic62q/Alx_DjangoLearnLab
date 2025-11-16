# LibraryProject/bookshelf/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# ----------------------------
# Custom User Model
# ----------------------------
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

# ----------------------------
# Book model with custom permissions
# ----------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title

# ----------------------------
# Signal to create groups and assign permissions
# ----------------------------
@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    """
    Create groups and assign custom permissions automatically after migrations
    """
    group_permissions = {
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        'Editors': ['can_view', 'can_create', 'can_edit'],
        'Viewers': ['can_view'],
    }

    for group_name, perms in group_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm_codename in perms:
            try:
                permission = Permission.objects.get(codename=perm_codename)
                group.permissions.add(permission)
            except Permission.DoesNotExist:
                print(f"Permission {perm_codename} does not exist yet.")
        group.save()
