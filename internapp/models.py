from django.db import models

# Create your models here.
class Account_Details(models.Model):
    #<csrf token>
    First_Name = models.CharField(max_length = 30)
    Last_Name = models.CharField(max_length = 30)
    Emails = models.CharField(max_length = 50)
    Contact_no = models.IntegerField(12)
    Address =models.TextField()