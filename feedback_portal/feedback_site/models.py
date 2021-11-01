# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Feedback(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 128 )
    image = models.URLField(blank = True)
    category = models.CharField(max_length=32 ,blank = True)
    creator = models.ForeignKey(User, related_name= 'owner' ,on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.title} - {self.description} - {self.category}'

