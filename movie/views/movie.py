from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movie.models import Movie, MovieTurn
from movie.serializers import MovieSerializer, MovieTurnSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]


class MovieTurnViewSet(viewsets.ModelViewSet):
    queryset = MovieTurn.objects.all()
    serializer_class = MovieTurnSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['turn', 'movie']
