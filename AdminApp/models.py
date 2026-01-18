from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="images",null=True,blank=True)
    Location=models.TextField(max_length=100,null=True,blank=True)

class CompanyDB(models.Model):
    Category_Name = models.CharField(max_length=100,null=True,blank=True)
    Company_Name = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)


class JobDB(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Company_Name=models.CharField(max_length=100,null=True,blank=True)
    Job_Location=models.CharField(max_length=100,null=True,blank=True)
    Job_Role=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(max_length=100,null=True,blank=True)
    Job_Type=models.TextField(max_length=100,null=True,blank=True)
    Logo=models.ImageField(upload_to="logos",null=True,blank=True)
    Job_Date=models.DateField(max_length=100,null=True,blank=True)
