from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField( max_length=50)
    email =models.EmailField(max_length=254)
    password=models.CharField( max_length=50)
    phonenumber = models.IntegerField()
    address = models.TextField()

    def _str_(self):
        return self.user.username
