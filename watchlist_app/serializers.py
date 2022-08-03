from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField(max_length=100)
   description = serializers.CharField(max_length=200)
   is_active =serializers.BooleanField(default=True)
   
   def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

   def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.name)
        instance.descrition = validated_data.get('code', instance.description)
        instance.is_active = validated_data.get('linenos', instance.is_active)
        instance.save()
        return instance