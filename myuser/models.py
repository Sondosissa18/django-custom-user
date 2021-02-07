from django.db import models


from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import User



class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(max_length=200)



    def __str__(self):
        return self.username