from django.db import models
from .utils import GENRE_CHOICES
from uuid import uuid4

class Filme(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=255)
  year = models.IntegerField()
  date_published = models.DateField()
  min_duration = models.IntegerField()
  country = models.CharField(max_length=255)
  director = models.CharField(max_length=255)
  writer = models.CharField(max_length=255)
  production_company = models.CharField(max_length=255)
  description = models.TextField()
  avg_vote = models.DecimalField(max_digits=10, decimal_places=2)
  budget = models.DecimalField(max_digits=50, decimal_places=2)
  genre = models.CharField(max_length=55, choices=GENRE_CHOICES, blank=False, null=False)

  def __str__(self) -> str:
    return self.title