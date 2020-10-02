from rest_framework import serializers

from movie.models import Movie, MovieTurn


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieTurnSerializer(serializers.ModelSerializer):
    turn_time = serializers.TimeField(source='turn.turn', read_only=True)

    class Meta:
        model = MovieTurn
        fields = '__all__'
