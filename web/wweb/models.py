from django.db import models

# Create your models here.
class Students(models.Model):
    stud_id=models.
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

    

class Result(models.Model):
    roll_num=models.ForeignKey(Students,on_delete=models.CASCADE)
    fl=models.DecimalField(max_digits=3,decimal_places=0)
    sl=models.DecimalField(max_digits=3,decimal_places=0)
    hindi=models.DecimalField(max_digits=3,decimal_places=0)
    ss=models.DecimalField(max_digits=3,decimal_places=0)
    maths=models.DecimalField(max_digits=3,decimal_places=0)
    science=models.DecimalField(max_digits=3,decimal_places=0)



