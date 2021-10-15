# Generated by Django 3.2.8 on 2021-10-14 19:37

from django.db import migrations
import pandas as pd

planilha = pd.read_excel('D:/Repositorio/Analise_de_dados/IMD_ movies/filmes.xlsx') 


def create_data(apps, schema_editor):
  Filme = apps.get_model('filmes', 'Filme')

  for index, row in planilha.iterrows():   

    Filme(
      title=row['original_title'], year=row['year'], date_published=row['date_published'], 
      min_duration=row['duration'], country=row['country'], director=row['director'], 
      writer=row['writer'], production_company=row['production_company'], 
      description=row['description'], avg_vote=row['avg_vote'], 
      budget=row['budget'], genre=row['genre']
    ).save()


class Migration(migrations.Migration):

  dependencies = [
      ('filmes', '0001_initial'),
  ]

  operations = [
    migrations.RunPython(create_data),
  ]
