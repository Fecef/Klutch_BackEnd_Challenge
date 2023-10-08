import django_filters

from .models import Solicitation


class SolicitationFilter(django_filters.FilterSet):
    cpf = django_filters.CharFilter(field_name="client__cpf", lookup_expr="exact")

    class Meta:
        model = Solicitation
        fields = ["cpf"]
