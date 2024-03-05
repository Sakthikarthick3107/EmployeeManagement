from django.db import models

# Create your models here.

class Department(models.Model):
    
    dept = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.dept
    
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    dept = models.ForeignKey(Department , on_delete=models.CASCADE , related_name='department')
    salary = models.DecimalField(max_digits=10 , decimal_places=2)
    native = models.CharField(max_length=20)
    

