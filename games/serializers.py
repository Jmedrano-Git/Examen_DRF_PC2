from rest_framework import serializers
from .models import CompanyDb, GameDb

class GameListSerializer(serializers.ModelSerializer):
    #El campo de solo lectura para mostrar el nombre de la compañía (Punto extra)
    company_name = serializers.CharField(source='company.name', read_only=True)