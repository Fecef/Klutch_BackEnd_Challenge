import django_filters

from .models import Client


class ClientFilter(django_filters.FilterSet):
    cpf = django_filters.CharFilter(field_name="cpf", lookup_expr="exact")

    class Meta:
        model = Client
        fields = ["cpf"]
