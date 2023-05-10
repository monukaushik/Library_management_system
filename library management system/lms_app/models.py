from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import *

class Userdetail(AbstractBaseUser,PermissionsMixin):
        email=models.EmailField(unique=True)
        username=models.CharField(max_length=100)
        studentimg=models.ImageField(upload_to='images/', default='images.png')
        studentbranch=models.CharField(max_length=100)
        studentrollno=models.IntegerField(null=True,blank=True)
        studentadd1=models.CharField(max_length=200)
        is_staff=models.BooleanField(default=False)
        is_active=models.BooleanField(default=True)

        objects=CustomuserdetailManager()

        USERNAME_FIELD='email'
        REQUIRED_FIELDS=['username']

        def __str__(self):
            return self.email 

class bookdetail(models.Model):
    bookid=models.AutoField(primary_key=True)
    bookname=models.CharField(max_length=200)
    stuname=models.CharField(max_length=200,null=True)
    sturollno=models.IntegerField(null=True)
    bookimage=models.ImageField(upload_to='images/')
    bookauthor=models.CharField(max_length=200)
    branch=models.CharField(max_length=100)
    price=models.IntegerField()
    Qty= models.IntegerField()
    requiredqty=models.IntegerField(null=True)
    status=models.CharField(max_length=100)
    issuedate=models.DateTimeField(null=True) 

    def __str__(self):
        return self.bookname 

        



