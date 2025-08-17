# api/serializers.py
from rest_framework import serializers
from .models import Tower

class TowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tower
        fields = ['id', 'owner', 'name', 'location', 'height_m', 'tower_type', 'created_at']
        read_only_fields = ['id', 'created_at']