from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.TextField()
    mother_name=models.TextField()
    father_name=models.TextField()
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=7)
    date=models.DateField()
    course=models.TextField()
    contact=models.TextField()

