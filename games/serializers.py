from rest_framework import serializers
from .models import CompanyDb, GameDb

class GameListSerializer(serializers.ModelSerializer):
    #El campo de solo lectura para mostrar el nombre de la compañía (Punto extra)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = GameDb
        fields = ['id', 'title', 'genre', 'release_year', 'company', 'company_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'company_name']
    

class CompanyNestedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDb
        fields = ['id', 'title', 'genre', 'release_year']


class CompanySerializer(serializers.ModelSerializer):
    # Acá muestra los juegos relacionados en la representación de company (GET /companies/)
    games = CompanyNestedGameSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyDb
        fields = ['id', 'name', 'country', 'games', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']