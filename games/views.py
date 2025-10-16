from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import GameDb, CompanyDb
from .serializers import GameListSerializer, CompanySerializer

class GameViewSet(viewsets.ModelViewSet):
    # Los endpoints(Get,Post,el GET/id o el PUT/id, el DELETE/id o buscar los datos que ponga por su titulo o el genero)
    # Usando ?search=juego1xd como ejemplo
    queryset = GameDb.objects.select_related('company').all()
    serializer_class = GameListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'genre'] #Aquí permite el ?search=juego1xd

class CompanyViewSet(viewsets.ModelViewSet):
    # Lo mismo todos los endpoints pero aquí ya muestra los juegos que pertenecen a cada compañía 
    queryset = CompanyDb.objects.prefetch_related('games').all()
    serializer_class = CompanySerializer