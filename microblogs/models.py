from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ follwed by at least three alphanumbericals'
        )]
    )
    bio = models.CharField(max_length = 520)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank = False)
    text = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)

    class Meta:
        ordering = ['-created_at']
