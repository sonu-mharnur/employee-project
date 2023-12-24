from django.db import models

# Create your models here.

class employeeData(models.Model):
    emp_name = models.CharField('emp name',max_length=200)
    emp_id = models.CharField('emp id')
    emp_contact = models.IntegerField('emp contact')
    emp_work = models.CharField('emp work',max_length=50)
    emp_email = models.EmailField('emp email',max_length=50) 

def __str__(self):
    return self. emp_name()

class companyData(models.Model)