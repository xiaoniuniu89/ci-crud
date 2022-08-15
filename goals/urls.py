from django.urls import path
from .views import (
    goals_list,
    update_goal,
    delete_goal,
    GoalsListView,
    GoalCreateView,
    GoalUpdateView,
    GoalDeleteView,
)

urlpatterns = [
    # func views 
    path('', goals_list, name="goals_list"),
    path('update-goal/<int:pk>/', update_goal, name="update_goal"),
    path('delete-goal/<int:pk>/', delete_goal, name="delete_goal"),
    # cbv views 
    path('cbv/', GoalsListView.as_view(), name="goals_list_cbv"),
    path('cbv/create/', GoalCreateView.as_view(), name="goal_create_cbv"),
    path('cbv/update/<int:pk>/', GoalUpdateView.as_view(), name="goal_update_cbv"),
    path('cbv/delete/<int:pk>/', GoalDeleteView.as_view(), name="goal_delete_cbv"),
    
]