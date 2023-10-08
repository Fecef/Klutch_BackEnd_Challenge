from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .filters import SolicitationFilter
from .models import Solicitation
from .serializers import SolicitationSerializer


class SolicitationView(generics.ListCreateAPIView):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SolicitationFilter
