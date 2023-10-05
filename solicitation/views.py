from rest_framework import generics

from .models import Solicitation
from .serializers import SolicitationSerializer


class SolicitationView(generics.ListCreateAPIView):
    queryset = Solicitation.objects.all()
    serializer_class = SolicitationSerializer
