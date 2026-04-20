from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # ❌ bỏ những field không dùng
    first_name = None
    last_name = None

    # ✅ thêm field cần thiết
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("operator", "Operator"),
        ("user", "User"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="user"
    )

    # dùng username để login
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username