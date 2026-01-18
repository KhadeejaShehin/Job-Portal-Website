from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)

class SignupDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)



from django.db import models

class AppliedDB(models.Model):
    Username = models.CharField(max_length=150, null=True, blank=True)  # Add this field
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Education = models.CharField(max_length=150, null=True, blank=True)
    Experience = models.IntegerField(null=True, blank=True)
    Skills = models.TextField(null=True, blank=True)
    Resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    Company_name = models.CharField(max_length=150, null=True, blank=True)
    Job_role = models.CharField(max_length=150, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)

