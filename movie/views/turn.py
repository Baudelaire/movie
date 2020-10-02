from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movie.models import Turn
from movie.serializers import TurnSerializer


class TurnViewSet(viewsets.ModelViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer
    permission_classes = [IsAuthenticated]
