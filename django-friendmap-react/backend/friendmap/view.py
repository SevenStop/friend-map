from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FriendmapSerializer
from .models import Friendmap

# Create your views here.

class FriendmapView(viewsets.ModelViewSet):
    serializer_class = FriendmapSerializer
    queryset = Friendmap.objects.all()