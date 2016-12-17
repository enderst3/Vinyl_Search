from rest_framework import serializers
from .models import VinylQuery


class VinylQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VinylQuery
        fields = ('query_image', 'imgur_url', 'user', 'created', 'result_title',
                  'result_thumb')
