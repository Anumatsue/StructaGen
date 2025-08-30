from rest_framework import serializers
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

class TowerSerializer(serializers.ModelSerializer):
    antennas = AntennaSerializer(many=True, read_only=True)
    stress_results = StressResultSerializer(many=True, read_only=True)

    class Meta:
        model = Tower
        fields = ["id", "owner", "name", "location", "height_m", "tower_type", "antennas", "stress_results"]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Tower.objects.create(owner=user, **validated_data)

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["id", "owner", "tower", "created_at", "title", "metadata"]
        read_only_fields = ["owner", "docx_file", "created_at", "metadata"]


