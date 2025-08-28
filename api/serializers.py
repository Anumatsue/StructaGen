from rest_framework import serializers
<<<<<<< HEAD
from .models import Tower, Antenna, StressResult, Report

class AntennaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antenna
        fields = "__all__"
        read_only_fields = ("epa", "fpa", "tower")

class StressResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StressResult
        fields = "__all__"
        read_only_fields = ("tower",)
=======
from .models import Tower, Report
>>>>>>> feature/reports-api

class TowerSerializer(serializers.ModelSerializer):
    antennas = AntennaSerializer(many=True, read_only=True)
    stress_results = StressResultSerializer(many=True, read_only=True)

    class Meta:
        model = Tower
<<<<<<< HEAD
        fields = ["id", "owner", "name", "location", "height_m", "tower_type", "antennas", "stress_results"]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Tower.objects.create(owner=user, **validated_data)

=======
        fields = ['id', 'owner', 'name', 'location', 'height_m', 'tower_type', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    
    def create(self, validated_data):
        user = self.context["request"].user
        return Tower.objects.create(owner=user, **validated_data)
    
>>>>>>> feature/reports-api
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["id", "owner", "tower", "docx_file", "created_at", "title", "metadata"]
        read_only_fields = ["owner", "docx_file", "created_at"]
