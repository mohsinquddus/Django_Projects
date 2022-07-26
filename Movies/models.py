from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    genree = models.CharField(max_length=256)

    def __str__(self):
        return self.genree
    
class Movies(models.Model):
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    stock = models.IntegerField()
    duration = models.IntegerField()
    created_date = models.DateField(default=timezone.now)
    genre = models.ForeignKey(Genre, default='Mohsin', on_delete=models.CASCADE)
