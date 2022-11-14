from rest_framework import serializers
from .models import Artiste, Song


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id', 'first_name', 'last_name', 'age']  # same as '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'Artiste', 'title', 'date_released',
                  'likes', 'artiste_id']  # same as '__all__'
