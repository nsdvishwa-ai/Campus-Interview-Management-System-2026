from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=30, unique=True)
    department = models.CharField(max_length=50)
    cgpa = models.FloatField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    package = models.FloatField()
    eligibility_cgpa = models.FloatField()
    deadline = models.DateField()

    def __str__(self):
        return self.company_name


class PasswordChangeLog(models.Model):
    username = models.CharField(max_length=100)
    old_password = models.CharField(max_length=100)
    new_password = models.CharField(max_length=100)
    changed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class LoginHistory(models.Model):
    username = models.CharField(max_length=100)
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return self.username