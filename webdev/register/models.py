from django.db import models

# Create your models here.

from django.contrib.auth.models import User
class User_changes(User):
    phone=models.IntegerField()
    cell=models.CharField(max_length=32,default='')

    def __str__(self):
        return self.username
   