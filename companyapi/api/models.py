from django.db import models

# Create your models here.

# Creating Company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(
        max_length=30,
        choices=(
            ('IT', 'IT'),
            ('NON IT', 'NON IT'),
            ('Mobile Phones', 'Mobile Phones')
        )
    )    
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.location



# Creating Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    about = models.TextField()
    position = models.CharField(
        max_length=50,
        choices=(
            ('Manager', 'Manager'),
            ('Software Developer', 'SD'),
            ('Project Lead', 'PL')
        )
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)




