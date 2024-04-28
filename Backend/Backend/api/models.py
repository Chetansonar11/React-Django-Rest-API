from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    grade = models.CharField(max_length=6)
    address = models.TextField()
    contact_number = models.IntegerField()

    def __str__(self):
        return self.first_name
    

