from django.db import models

# Create your models here.

class Department (models.Model):
    name = models.CharField(max_length=100, null=False)
    location  = models.CharField(max_length=100, null = True)
    teamLead = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    numberOfEmployees = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Employee (models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


# instead of seeing employee object, i want to see first and last names on the employee list,so these 2 lines of code is writtten
    def __str__(self):
        return self.firstName + ' ' + self.lastName




#object1 = Employee()
#object1.firstName = 'Raj'
# #object1.lastName = 'srirangam'
# #object1.save() # here save() is not defined but inherited from Model

#object2 = Employee()
# #object2.firstName = 'Rajesh'
#object2.lastName = 'gaddam'
#object2.save()


