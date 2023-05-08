from django.db import models

# Create your models here.

#Company Models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about= models.CharField(max_length=50)
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones',"Mobile Phones")))
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
       return self.name;

#For company name show



#Employee Models
class Employee (models.Model):
    employee_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    about =models.TextField()
    position= models.CharField(max_length=50,choices=(("manager",'manager'),('software','sd'),('project leader','pl')))
    
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
