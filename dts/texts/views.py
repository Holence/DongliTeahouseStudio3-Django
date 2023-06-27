from rest_framework import viewsets, permissions
from .models import Text
from .serializers import TextSerializer

class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = [permissions.IsAuthenticated]
