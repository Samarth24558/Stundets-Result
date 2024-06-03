from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=200)
    mother_name=models.CharField(max_length=200)
    father_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=7)
    date=models.DateField()
    course=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)

    def __str__(self):
        return self.name

