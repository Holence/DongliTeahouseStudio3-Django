from rest_framework import serializers

from .models import Attachment

class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = [
            "date",
            "name",
            "texts",
            "concepts",
        ]
