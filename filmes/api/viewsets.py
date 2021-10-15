from rest_framework import viewsets
from filmes.api.serializers import FilmeSerializer
from filmes.models import Filme
import django_filters

class FilmeFilter(django_filters.FilterSet):
  title = django_filters.CharFilter(lookup_expr='icontains')

  class Meta:
    model = Filme
    fields = ['title', 'genre']

class FilmeViewSet(viewsets.ModelViewSet):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer
  filterset_class = FilmeFilter