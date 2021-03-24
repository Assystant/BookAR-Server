from django.db import models

# Create your models here.
class DemoModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)