from rest_framework import generics


from .permissions import IsAdmin
from .models import RateTable
from .serializers import RateTableSerializer


class RateTableView(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]

    queryset = RateTable.objects.all()
    serializer_class = RateTableSerializer
