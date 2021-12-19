from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from .choices import DOCTOR_STATUS

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    status = models.IntegerField(DOCTOR_STATUS, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Admin_Helath_CSV(models.Model):
    name = models.CharField(max_length=100, null=True)
    csv_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

class Search_Data(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    prediction_accuracy = models.CharField(max_length=100,null=True,blank=True)
    result = models.CharField(max_length=100,null=True,blank=True)
    values_list = models.CharField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.patient.user.username

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    messages = models.TextField(null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.user.username