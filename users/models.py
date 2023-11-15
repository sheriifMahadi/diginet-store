from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username