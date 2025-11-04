from django.db import models

# Create your models here.
class UsersTable(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=20,null=False)
    user_email=models.EmailField(max_length=30,default="user@gmail.com")
    user_phone=models.CharField(max_length=10,unique=True)
    