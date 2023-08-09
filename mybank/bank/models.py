from django.db import models

from django import forms

class Application(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField()
    Dob=models.DateField()
    gender=models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=650)
    def __str__(self):
        return self.name
