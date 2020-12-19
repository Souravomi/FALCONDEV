from django.db import models

# Create your models here.

class Response(models.Model):
    Name = models.CharField(max_length=200)
    EMail = models.CharField(max_length=300)
    Mobile = models.CharField(max_length=100,null=True)
    Service = models.CharField(max_length=100,null=True)
    Need = models.CharField(max_length=200,null=True)
    Language = models.CharField(max_length=200,default='Null',null=True)
    Description = models.CharField(max_length=500,null=True)
    Status = models.CharField(max_length=50,default='Submitted',null=True)
    Appl_Date = models.DateField(auto_now=True,null=True)
