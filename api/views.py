from django.shortcuts import render

# api/views.py
from rest_framework import viewsets, permissions
from .models import Tower
from .serializers import TowerSerializer
 

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
<<<<<<< Updated upstream
        # Ensure the logged-in user is set as the owner
        serializer.save(owner=self.request.user)
=======
        tower_id = self.request.data.get("tower")
        tower = get_object_or_404(Tower, pk=tower_id, owner=self.request.user)
        obj = serializer.save(tower=tower)
        obj.calculate_epa_fpa()
        obj.save()

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return self.request.user.reports.all()

>>>>>>> Stashed changes
