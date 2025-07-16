from rest_framework import serializers
from .models import Brief

class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brief
        fields = ['id', 'file', 'description', 'created_by', 'created_at']
        read_only_fields = ['description', 'created_by', 'created_at']
