from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

class BaseClass(models.Model):
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
    updated_by = models.CharField(max_length=50, null=True, default=None)

    class Meta:
        abstract = True


class CV(BaseClass):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    mobID = models.CharField(max_length=10,primary_key=True)
    group1 = models.CharField(max_length=30,null=False, default=None)
    salutation= models.CharField(max_length=4,choices=[("Mr.","Mr."),
                                                       ("Ms.","Ms."),
                                                       ("Mrs.","Mrs.")])
    firstname = models.CharField(max_length=40,null=False, default=None)
    primaryNumber = models.CharField(max_length=20,null=False, default=None)
    primaryMail = models.EmailField(max_length=80,null=False, default=None)
    city = models.CharField(max_length=30,null=False, default=None)
    country = CountryField(blank=True)
    pincode = models.CharField(max_length=12,null=False, default=None)
    image1=models.ImageField(upload_to='cv',default=None)
    donotCall=models.BooleanField(null=False, default=None)

    def __str__(self):
        return self.firstname
    
    class Meta:
        db_table="MobDb"

