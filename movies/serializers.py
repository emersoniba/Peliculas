from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year')
        
    def validate_title(self,value):
        return value.upper().strip()
    

