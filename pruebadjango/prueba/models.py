
# Create your models here.
from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=30,blank=False)
	email= models.CharField(max_length=30,blank=False)
	
	class Meta:
        abstract = True

class Customer(Actor):
    

	
class User(Actor):
    

	
class Business(models.Model):
    owner = models.ForeignKey(Custormer)
    name = models.CharField(max_length=20,blank=False)
    description = models.CharField(Max_length=300,blank=False)
	
	
class UserAccount(models.Model):
    user = models.ForeignKey(Actor)
    username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)