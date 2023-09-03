from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ACCOUNT_TYPE = (
    ('Doctor','Doctor'),
    ('Patient','Patient'),
    ('Admin','Admin'),
    ('User','User'),
    ('Technologist','Technologist'),
    ('Recieptionist','Recietionist'),
    ('Accounce','Accounce'),
    ('Cash','Cash'),
)
GENDER_TYPE = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)
class UserHospitalManagement(models.Model):
    username = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20,choices=ACCOUNT_TYPE)
    employee_id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    
 
    
class UserDetails(models.Model):
    username = models.OneToOneField(User,related_name='user_details',on_delete=models.CASCADE)
    house = models.CharField(max_length=1000,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    mobile = models.IntegerField()

