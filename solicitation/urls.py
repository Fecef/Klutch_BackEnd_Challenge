from django.urls import path

from .views import SolicitationView

urlpatterns = [
    path("solicitation/", SolicitationView.as_view()),
]
