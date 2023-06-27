from rest_framework import serializers

from .models import Concept

class ConceptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Concept
        fields = [
            "name",
            "description",
            "childs",
            "relatives",
            "texts",
            "attachments",
        ]
