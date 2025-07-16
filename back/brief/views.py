from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Brief
from .serializers import BriefSerializer
from .utils import analyze_file

class BriefViewSet(viewsets.ModelViewSet):
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        brief = serializer.save(created_by=self.request.user)
        description = analyze_file(brief.file.path)
        brief.description = description
        brief.save()
