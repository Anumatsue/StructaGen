from django.shortcuts import render

# api/views.py
from rest_framework import viewsets, permissions
from .models import Tower
from .serializers import TowerSerializer
 

class TowerViewSet(viewsets.ModelViewSet):
    queryset = Tower.objects.all()
    serializer_class = TowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the logged-in user is set as the owner
        serializer.save(owner=self.request.user)
