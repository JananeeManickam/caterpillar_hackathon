from rest_framework import serializers
from .models import Brief
from .utils import generate_brief_from_file

class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brief
        fields = ['id', 'file', 'description']
        read_only_fields = ['description']

    def create(self, validated_data):
        instance = Brief.objects.create(**validated_data)
        # Now the file is saved, we can safely access the path
        if instance.file:
            instance.description = generate_brief_from_file(instance.file.path)
            instance.save(update_fields=['description'])
        return instance

    def update(self, instance, validated_data):
        instance.file = validated_data.get('file', instance.file)
        instance.save()  # save file to disk first
        instance.description = generate_brief_from_file(instance.file.path)
        instance.save(update_fields=['description'])
        return instance
