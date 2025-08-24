# api/serializers.py
from rest_framework import serializers
from .models import Tower, Report

class TowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tower
        fields = ['id', 'owner', 'name', 'location', 'height_m', 'tower_type', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    
    def create(self, validated_data):
        user = self.context["request"].user
        return Tower.objects.create(owner=user, **validated_data)
    
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["id", "owner", "tower", "docx_file", "created_at", "title", "metadata"]
        read_only_fields = ["owner", "docx_file", "created_at"]
