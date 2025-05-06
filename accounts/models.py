from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_picture')
    
    def __str__(self):
        return self.user.username
    
class Addeducation(models.Model):
    School = models.CharField(max_length=50)
    Degree = models.CharField(max_length=50)
    Field = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null = True,blank=True)
    description = models.TextField()
    
class Addexperience(models.Model):
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True,blank=True)
    description = models.TextField()