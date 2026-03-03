from django.db import models

# Create your models here.
# Creating company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT', 'IT'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare'), ('Education', 'Education')))
    added_date = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50, choices=(('Manager', 'Manager'), ('Developer', 'Developer'), ('Designer', 'Designer'), ('Analyst', 'Analyst')))
    hire_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    company=models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)