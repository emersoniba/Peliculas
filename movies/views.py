from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer

@extend_schema(tags=['Gestion API Movies'])
class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    permission_classes=[IsAuthenticated ]





