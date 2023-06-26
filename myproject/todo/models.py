from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
#string represetnation
    def __str__(self):
      return self.name
