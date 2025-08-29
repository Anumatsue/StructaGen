#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Tower, Antenna, StressResult, Report
from .serializers import TowerSerializer, AntennaSerializer, StressResultSerializer, ReportSerializer
from .permissions import IsOwner
from .services.report_generator import ReportGenerator

class TowerViewSet(viewsets.ModelViewSet):
    serializer_class = TowerSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.request.user.towers.all()

    @action(detail=True, methods=["post"])
    def generate_report(self, request, pk=None):
        tower = get_object_or_404(Tower, pk=pk, owner=request.user)
        include_stress = request.data.get("include_stress", True)
        generator = ReportGenerator(tower=tower, include_stress=include_stress, user=request.user)
        report_obj = generator.generate_and_save()
        serializer = ReportSerializer(report_obj, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AntennaViewSet(viewsets.ModelViewSet):
    serializer_class = AntennaSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        tower_id = self.kwargs.get("tower_pk") or self.request.query_params.get("tower")
        if tower_id:
            return Antenna.objects.filter(tower__owner=self.request.user, tower_id=tower_id)
        return Antenna.objects.filter(tower__owner=self.request.user)

    def perform_create(self, serializer):
        tower_id = self.request.data.get("tower")
        tower = get_object_or_404(Tower, pk=tower_id, owner=self.request.user)
        obj = serializer.save(tower=tower)
        obj.calculate_epa_fpa()
        obj.save()

class StressResultViewSet(viewsets.ModelViewSet):
    serializer_class = StressResultSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        tower_id = self.kwargs.get("tower_pk") or self.request.query_params.get("tower")
        if tower_id:
            return StressResult.objects.filter(tower__owner=self.request.user, tower_id=tower_id)
        return StressResult.objects.filter(tower__owner=self.request.user)

    def perform_create(self, serializer):
        tower_id = self.request.data.get("tower")
        tower = get_object_or_404(Tower, pk=tower_id, owner=self.request.user)
        serializer.save(tower=tower)

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.request.user.reports.all()


