from django.db import models
from django.contrib.auth.models import User


class VinylQuery(models.Model):
    query_image = models.ImageField()
    imgur_url = models.URLField(null=True)
    user = models.ForeignKey(User, related_name='searches')
    created = models.DateTimeField(auto_now=True)
    result_title = models.CharField(max_length=9000, null=True)
    result_thumb = models.URLField(null=True)
    #result_format = models.CharField(max_length=9000, null=True)
    

    def __str__(self):
        result = self.imgur_url
        # if statement so I can delete queries with no image in admin
        if result == None:
            return ''
        
        else:
            return result

    def __repr__(self):
        result = self.imgur_url
        return result

    
