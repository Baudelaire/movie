from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    image = models.ImageField(upload_to='movies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
