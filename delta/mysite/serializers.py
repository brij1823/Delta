from rest_framework import serializers
from .models import Categories

class getListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'img_url']