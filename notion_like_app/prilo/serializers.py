from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only = True)
    time_updated = serializers.DateTimeField(read_only = True)
    time_created = serializers.DateTimeField(read_only = True)

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Notes
        fields = ('__all__')