from unicodedata import name
from django.db import models

# Create your models here.
class Movie(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField(max_length=100)
   is_active = models.BooleanField(default=False)
   
   def __str__ (self):
      return self.name
   