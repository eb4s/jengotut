from pyexpat import model
from django.db import models

# Create your models here.
class Student (models.Model):

    GRADES =(
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    )

    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    middlename = models.CharField(max_length=200, null=True)
    grade = models.CharField(max_length=200, null=True, choices=GRADES)

    def __str__(self):
        return "" + str(self.lastname) + ", " + str(self.firstname)