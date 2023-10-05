from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from client.filters import ClientFilter


from .models import Client
from .serializers import ClientSerializer
from .permissions import IsAdmin


class ClientView(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter
