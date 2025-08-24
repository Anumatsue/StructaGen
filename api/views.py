from django.shortcuts import render

# api/views.py
from rest_framework import viewsets, permissions
from .models import Tower, Report
from .serializers import TowerSerializer, ReportSerializer
from .permissions import IsOwner
 

class TowerViewSet(viewsets.ModelViewSet):
    queryset = Tower.objects.all()
    serializer_class = TowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure the logged-in user is set as the owner
        serializer.save(owner=self.request.user)


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.request.user.reports.all()

