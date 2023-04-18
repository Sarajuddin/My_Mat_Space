from django.db import models

# Create your models here.
class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  mobile = models.CharField(max_length=20)
  age = models.CharField(max_length=5)
  gender = models.CharField(max_length=20)
  disease = models.CharField(max_length=50)
