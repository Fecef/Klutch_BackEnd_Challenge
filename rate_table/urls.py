from django.urls import path

from .views import RateTableView

urlpatterns = [
    path("rate_table/", RateTableView.as_view()),
]
