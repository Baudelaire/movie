from rest_framework import serializers

from movie.models import Turn


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'
