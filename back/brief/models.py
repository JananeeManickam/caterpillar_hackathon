from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from os.path import splitext

def validate_file_type(value):
    allowed_types = ['.pdf', '.docx', '.xlsx', '.csv']
    ext = splitext(value.name)[1]
    if ext.lower() not in allowed_types:
        raise ValidationError(f"Unsupported file type: {ext}. Allowed types: {', '.join(allowed_types)}")

class Brief(models.Model):
    file = models.FileField(upload_to='uploads/briefs/', validators=[validate_file_type])
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Brief {self.id} by {self.created_by}"
