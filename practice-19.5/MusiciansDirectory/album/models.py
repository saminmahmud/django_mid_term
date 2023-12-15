from django.db import models
from musician.models import Musician

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ]
    rating = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self):
        return self.album_name
