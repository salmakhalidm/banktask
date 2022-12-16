from django.db import models


class Task(models.Model):
    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )

    boolmat = (
        ("C", "Credit Card"), ("D", "Debit Card"),("Ch","cheque")
    )
    booldist = (
        ("Idukii", "Idukii"), ("Ernakulam", "Ernakulam"), ("Kollam", "Kollam")
    )

    boolbr = (
        ("Devikulam", "Devikulam"), ("Thodupuzha", "Thodupuzha"), ("Peerimeedu", "Peerimeedu"),("Kuttikanam", "Kuttikanam"), ("ALuva", "ALuva"), ("Edapally", "Edapally"),("Kothamangalam", "Kothamangalam"), ("Perumbavoor", "Perumbavoor"), ("Karunagappally", "Karunagappally"),("Kottarakara", "Kottarakara"),("Pathanapuram", "Pathanapuram"),("Kunnathur", "Kunnathur")
    )

    boolac = (
        ('Savings','Savings'),('Current','Current')
    )
    name=models.CharField(max_length=250)
    age=models.IntegerField(null=True, blank=True)
    dob=models.DateField()
    gender = models.CharField(max_length = 1,choices=boolChoice)
    txt = models.TextField()
    phone = models.IntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    materials = models.CharField(max_length=20,choices=boolmat, default=None)
    materialss = models.CharField(max_length=20,choices=boolmat,default=None)
    materialsq = models.CharField(max_length=20,choices=boolmat,default=None)
    subject = models.CharField(max_length=30, choices=booldist)
    topic = models.CharField(max_length=250, choices=boolbr)
    account=models.CharField(max_length=30, choices=boolac)





    def __str__ (self):
        return self.name
