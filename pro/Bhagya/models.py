from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)    
    message=models.CharField(max_length=500)

    def __str__(self):
        return "Massege from : " + self.name + " and email is : "+ self.email