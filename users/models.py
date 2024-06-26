from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    
    
    def __str__(self):
        return str(self.username)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return str(self.user)