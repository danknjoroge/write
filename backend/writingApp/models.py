from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Create your models here.
class User(AbstractUser):
    '''Boolean fields to select the type of account'''
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Admin(models.Model):
    '''Fields that will be contained in the Admin model/table in the database'''
    user = models.OneToOneField(User, related_name='admin', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

class Client(models.Model):
    '''Fields that will be contained in the Client model/table in the database'''
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    

class Writer(models.Model):
    '''Fields that will be contained in the Writer model/table in the database'''
    user = models.OneToOneField(User, related_name='writer', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    



