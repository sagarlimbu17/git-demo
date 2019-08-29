from django.db import models

# Create your models here.

class Employee(models.FormModel):
    name = models.CharField(max_length=255)
    