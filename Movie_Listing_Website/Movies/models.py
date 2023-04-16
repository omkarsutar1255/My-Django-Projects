from django.db import models


# Create your models here.
class MoviesData(models.Model):
    Name = models.CharField(max_length=50)
    Budget = models.IntegerField()
    Description = models.CharField(max_length=200)
    Genres = models.CharField(max_length=50)
    Popularity = models.FloatField(max_length=20)
    Revenue = models.IntegerField()
    Duration = models.IntegerField()
    Language = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    Release_Date = models.DateField()

    def __str__(self):
        return f'{self.Name}'
