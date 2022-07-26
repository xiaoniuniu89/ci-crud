from django.urls import path
from .views import (
    goals_list
)

urlpatterns = [
    path('', goals_list, name="goals_list"),
]