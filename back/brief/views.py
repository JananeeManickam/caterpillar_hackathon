from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile

class FileUploadView(APIView):
    def post(self, request):
        files = request.FILES.getlist('files')
        
        if not files:
            return Response({
                'error': 'No files uploaded.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Process uploaded files
        uploaded_files = []
        for file in files:
            try:
                uploaded_file = UploadedFile.objects.create(file=file)
                
                uploaded_files.append({
                    'id': uploaded_file.id,
                    'filename': uploaded_file.filename,
                    'size': uploaded_file.file_size,
                    'extension': uploaded_file.file_extension,
                    'content_preview': uploaded_file.content[:200] + '...' if len(uploaded_file.content) > 200 else uploaded_file.content,
                    'uploaded_at': uploaded_file.uploaded_at
                })
                
            except Exception as e:
                return Response({
                    'error': f'Error processing file {file.name}: {str(e)}'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'message': f'Successfully uploaded {len(uploaded_files)} file(s)',
            'files': uploaded_files
        }, status=status.HTTP_201_CREATED)

    # @action()
    # def get_content(self, request):
    #     pass
    def get(self, request):
        """Get all uploaded files"""
        files = UploadedFile.objects.all()
        
        files_data = []
        for file in files:
            files_data.append({
                'id': file.id,
                'filename': file.filename,
                'size': file.file_size,
                'extension': file.file_extension,
                'content_preview': file.content[:200] + '...' if len(file.content) > 200 else file.content,
                'uploaded_at': file.uploaded_at
            })
        
        return Response({
            'files': files_data,
            'total': len(files_data)
        }, status=status.HTTP_200_OK)

class FileDetailView(APIView):
    def get(self, request, file_id):
        """Get specific file with full content"""
        try:
            file = UploadedFile.objects.get(id=file_id)
        except UploadedFile.DoesNotExist:
            return Response({
                'error': 'File not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        return Response({
            'id': file.id,
            'filename': file.filename,
            'size': file.file_size,
            'extension': file.file_extension,
            'full_content': file.content,
            'uploaded_at': file.uploaded_at
        }, status=status.HTTP_200_OK)
    
    def put(self, request, file_id):
        """Update file content"""
        try:
            file = UploadedFile.objects.get(id=file_id)
        except UploadedFile.DoesNotExist:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)

        new_content = request.data.get('content')
        if new_content is None:
            return Response({'error': 'No content provided'}, status=status.HTTP_400_BAD_REQUEST)

        file.content = new_content
        file.save()

        return Response({'message': 'File updated successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, file_id):
        """Delete a specific file"""
        try:
            file = UploadedFile.objects.get(id=file_id)
            filename = file.filename
            file.delete()
            return Response({
                'message': f'File {filename} deleted successfully'
            }, status=status.HTTP_200_OK)
        except UploadedFile.DoesNotExist:
            return Response({
                'error': 'File not found'
            }, status=status.HTTP_404_NOT_FOUND)