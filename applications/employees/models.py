from django.db import models
from applications.departments.models import Department

class Employee(models.Model):

    GENDER_CHOICES = (
        (None, 'Select gender'),
        ('0', 'Female'),
        ('1', 'Male'),
        ('2', 'Other'),
    )

    JOB_CHOICES = (
        (None, 'Select work position'),
        ('0', 'CEO'),
        ('1', 'Assistant Manager'),
        ('2', 'IT Department Manager'),
        ('3', 'Software Engineer'),
        ('4', 'Software Developer'),
        ('5', 'Administration Department Manager'),
        ('6', 'Public Accountant'),
        ('7', 'Sales Department Representative'),
        ('8', 'Seller'),
        ('9', 'Communication Department Representative'),
        ('10', 'Community Manager'),
        ('11', 'Graphic Designer'),
        ('12', 'HR Department Representative'),
        ('13', 'Recruiter'),
        ('14', 'Statistics Department Manager'),
        ('15', 'Data Analyst'),
        ('16', 'Marketing Department Manager'),
        ('17', 'Publicist'),
    )

    first_name = models.CharField(
        'First name', 
        max_length=50
    )
    last_name = models.CharField(
        'Last name', 
        max_length=50
    )
    full_name = models.CharField(
        'Full name',
        max_length=100,
        blank=True
    )
    passport = models.CharField(
        'Passport', 
        max_length=10, unique=True
    )
    email = models.EmailField(
        'Email', 
        max_length=80, 
        unique=True
    )
    phone = models.CharField(
        'Phone number', 
        max_length=15, 
        blank=True
    )
    gender = models.CharField(
        'Gender', 
        max_length=1, 
        choices=GENDER_CHOICES
    )
    date_of_birth = models.DateField(
        'Date of birth'
    )
    job = models.CharField(
        'Job', 
        max_length=2, 
        choices=JOB_CHOICES
    )
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='company', 
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = 'My Employee'


    def __str__(self):
        return str(self.id) + '. ' + self.first_name + ' ' + self.last_name