from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goal(models.Model):
   user = models.ForeignKey(User, related_name="goals", on_delete=models.CASCADE) # user.goals.all()
   body = models.CharField(max_length=128)

   def __str__(self):
      return self.body
