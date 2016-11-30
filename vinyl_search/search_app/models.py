from django.db import models
from django.contrib.auth.models import User


class VinylQuery(models.Model):
    query_image = models.ImageField()
    imgur_url = models.URLField(null=True)
    user = models.ForeignKey(User, related_name='searches')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        result = self.imgur_url
        return result

    def __repr__(self):
        result = self.imgur_url
        return result
