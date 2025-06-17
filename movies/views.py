from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Movie
from rest_framework.response import Response
from rest_framework import status

from .serializers import MovieSerializer

@extend_schema(tags=['Gestion API Movies'])
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['GET'], url_path='contar-infantiles')
    def contar_infantiles(self, request):
        try:
            queryset=Movie.objects
            infantil=queryset.filter(genre='infantil').count()
            data={
                'total_infantiles': infantil
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=True, methods=['PUT'], url_path='actualizar-anio')
    def actualizar_anio(self, request, pk=None):
        try:
            pelicula = self.get_object()
            nuevo_anio = request.data.get('year')
            if nuevo_anio:
                pelicula.year = nuevo_anio
                pelicula.save()
                return Response({'mensaje': 'Año actualizado'}, status=200)
            return Response({'error': 'Falta el campo year'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=400)