from django.db import models


class User(models.Model):
 first_name =models.CharField(max_length=10)
 last_name = models.CharField(max_length=10)
 company_name=models.CharField(max_length=40)
 email_address=models.EmailField(max_length=70)
 country =models.CharField(max_length=20)
 code =models.IntegerField(max_length=8)
 phone_number= models.IntegerField(max_length=13)
 password =models.CharField(max_length=30)
 
