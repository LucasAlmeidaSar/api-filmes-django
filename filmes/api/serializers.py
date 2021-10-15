from rest_framework import serializers
from filmes.models import Filme

# Serializers define the API representation.

class FilmeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Filme
    fields = '__all__'