from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=100)
    Doctor =models.CharField(max_length=20, default=None)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50) 

    def __str__(self):
        return self.title



