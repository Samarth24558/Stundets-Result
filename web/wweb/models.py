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
        return str(self.id)

    

class Result(models.Model):
    roll_num=models.ForeignKey(Students,on_delete=models.CASCADE,primary_key=True)
    fl=models.DecimalField(max_digits=3,decimal_places=0)
    sl=models.DecimalField(max_digits=3,decimal_places=0)
    hindi=models.DecimalField(max_digits=3,decimal_places=0)
    ss=models.DecimalField(max_digits=3,decimal_places=0)
    maths=models.DecimalField(max_digits=3,decimal_places=0)
    science=models.DecimalField(max_digits=3,decimal_places=0)
    
    def __str__(self):
        return str(self.roll_num)
    
    def total_marks(self):
        return self.fl + self.sl + self.hindi + self.ss + self.maths + self.science

    




