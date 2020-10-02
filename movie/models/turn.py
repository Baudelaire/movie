from django.db import models


class Turn(models.Model):
    turn = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'turn'

    def __str__(self):
        return self.turn


class MovieTurn(models.Model):
    turn = models.ForeignKey(
        Turn, on_delete=models.CASCADE, related_name='movies'
    )
    movie = models.ForeignKey(
        'movie.Movie', on_delete=models.CASCADE, related_name='turns'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['turn', 'movie']
        ordering = ['turn']
        db_table = 'movie_turn'

    def __str__(self):
        return f'{self.movie}-{self.turn}'
