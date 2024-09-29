from django.db import models

# Database Seeding
class Department(models.Model):
    DeptName=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)

    def __str__(self):
        return self.DeptName
    
class Country(models.Model):
    CountryName=models.CharField(max_length=30)

    def __str__(self):
        return self.CountryName



# Create your models here.
class Empolyee(models.Model):

    COUNTRIES = [
        ('IND',"India"),
        ('AUS',"Australia"),
        ('UK',"United Kingdome"),
        ('USA',"United States of America"),
        ('JPN',"Japan")
    ]

    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Tilename=models.CharField(max_length=30)
    HasPassport=models.BooleanField()
    Salary=models.IntegerField()
    DOB=models.DateField()
    HireDate=models.DateField()
    Notes=models.CharField(max_length=200)
    #Country=models.CharField(max_length=35,choices=COUNTRIES,default=None)
    Email=models.EmailField(default=None,max_length=50)

    #Creating a foreing key
    # here models.PROTECT helps in : if by mistake or on purpose delete the recodr in the master table in this case Departments class
    # it will stop you from deleting the record in child table in this case Employee class
    EmpDeparment=models.ForeignKey("Department",default=0,on_delete=models.PROTECT)
    EmpCountry=models.ForeignKey("Country",default=0,on_delete=models.PROTECT)

class PartTimeEmpolyee(models.Model):
    Firstname=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Tilename=models.CharField(max_length=30)