from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class User_Login(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    EMail = models.CharField(max_length=300, unique=True, primary_key=True)
    Name = models.CharField(max_length=200)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Designation = models.CharField(max_length=30)
    Addre_1 = models.CharField(max_length=70)
    Addre_2 = models.CharField(max_length=70)
    Addre_3 = models.CharField(max_length=70)
    Pin = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=50)
    #Password = models.CharField(max_length=70)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    last_login = models.DateTimeField()
    Status = models.CharField(max_length=70,default='Active')
    



class User_Updates(models.Model):
    User_id = models.ForeignKey(User_Login,on_delete=models.CASCADE)
    Subject = models.CharField(max_length=50)
    Issue = models.CharField(max_length=50,blank=True,null=True)
    Desc = models.TextField(max_length=200)



class Templ_Contact(models.Model):
    EMail = models.CharField(max_length=50,null=True)
    Mobile = models.CharField(max_length=12,null=True)



class Templ_Technologies(models.Model):
    Language = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Image = models.ImageField(default='default.jpg',upload_to='Technologies')
    Status = models.CharField(max_length=70)
    Owner = models.CharField(max_length=200)
    Added_On = models.DateField(auto_now=True)



class Templ_Services(models.Model):
    Service = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000,null=True)
    Type = models.CharField(max_length=100)
    Status = models.CharField(max_length=70)
    Owner = models.CharField(max_length=200)
    Added_On = models.DateField(auto_now=True)


class Academic_Projects(models.Model):
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    Status = models.CharField(max_length=70)
    Date = models.DateField(auto_now=True)
    Description = models.CharField(max_length=500,null=True)


class Business_Works(models.Model):
    Name = models.CharField(max_length=200)
    Type = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Client_Name = models.CharField(max_length=100)
    Client_Contact = models.CharField(max_length=50,null=True)
    Client_Email = models.CharField(max_length=100,null=True)
    URL = models.CharField(max_length=500)
    Status = models.CharField(max_length=70)
    Date = models.DateField(auto_now=True)
    Description = models.CharField(max_length=500,null=True)

    

class Updations(models.Model):
    Update = models.CharField(max_length=100)
    Change = models.CharField(max_length=100,null=True)
    Owner = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now=True)

    