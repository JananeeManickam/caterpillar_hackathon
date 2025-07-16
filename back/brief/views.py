from rest_framework import viewsets
from .models import Brief
from .serializers import BriefSerializer
from .utils import edit_pdf
from rest_framework.decorators import action

import os
class BriefViewSet(viewsets.ModelViewSet):
    queryset = Brief.objects.all()
    serializer_class = BriefSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    # @action(detail=True, methods=['post'])
    # def edit(self, request, pk=None):
    #     brief = self.get_object()
    #     file_ext = os.path.splitext(brief.file.name)[1].lower()

    #     if file_ext == '.pdf':
    #         new_file = edit_pdf(brief.file)
    #     else:
    #         return Response({"error": "Editing supported only for PDFs now."}, status=400)

    #     filename = os.path.basename(brief.file.name)
    #     brief.file.save(name=filename, content=ContentFile(new_file.read()), save=True)
    #     brief.save()
    #     return Response({"status": "file updated successfully"})
