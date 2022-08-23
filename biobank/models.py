from pyexpat import model
from django.db import models

# Create your models here.



class Study(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE)
    # patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Patient(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) 
    dob = models.DateField(null=False)
    gender = models.CharField(max_length=10)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)



class Freezer(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    shelves = models.IntegerField()

class Shelf(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    racks = models.IntegerField()
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)

class Rack(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()


class Box(models.Model):
    _id = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    rack= models.ForeignKey(Rack, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)

class Cube(models.Model):
    _id = models.AutoField(primary_key=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    rack= models.ForeignKey(Rack, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    freezer = models.ForeignKey(Freezer, on_delete=models.CASCADE)


class Sample(models.Model):
    _id = models.AutoField(primary_key=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    date_of_archive = models.DateField(null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

