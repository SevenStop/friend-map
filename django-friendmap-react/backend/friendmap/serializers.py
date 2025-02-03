from rest_framework import serializers
from .models import Friendmap

class FriendmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendmap
        fields = ('id', 'title', 'description', 'completed')