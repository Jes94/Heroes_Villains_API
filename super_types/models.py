from django.db import models

# Create your models here.
class SuperType(models.Model):
    tpye = models.CharField(max_length=7)