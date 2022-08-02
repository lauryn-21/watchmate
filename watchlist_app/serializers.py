from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   name = serializers.CharField(max_length=100)
   description = serializers.CharField(max_length=200)
   is_active =serializers.BooleanField(default=True)
   