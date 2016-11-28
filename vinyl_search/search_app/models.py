from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VinylQuery(models.Model):

    query_image = models.ImageField()
    #user = models.ForeignKey(User, related_name='searches')

    def __str__(self):
        result = self.user.username
        return result


    def __repr__(self):
        result = self.user.username
        return result
