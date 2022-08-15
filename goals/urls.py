from django.urls import path
from .views import (
    goals_list,
    update_goal,
    delete_goal,
    GoalsListView
)

urlpatterns = [
    path('', goals_list, name="goals_list"),
    path('update-goal/<int:pk>/', update_goal, name="update_goal"),
    path('delete-goal/<int:pk>/', delete_goal, name="delete_goal"),
    path('cbv/', GoalsListView.as_view(), name="goals_list_cbv"),
    
]