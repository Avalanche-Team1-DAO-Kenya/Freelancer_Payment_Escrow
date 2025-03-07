from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
      email = models.EmailField(max_length=255, unique=True)
      password = models.CharField(max_length=255)
      username = None

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []

class Repo(models.Model):
      owner = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      framework = models.CharField(max_length=255)
      description = models.CharField(max_length=255)
      private = models.BooleanField(default=False)
      has_issues = models.BooleanField(default=False)
      has_projects = models.BooleanField(default=True)
      has_wiki = models.BooleanField(default=True)
