from django.urls import path
from .views import (
    goals_list,
    update_goal,
    delete_goal,
    Goals,
    GoalsListView,
    GoalDetailView,
    GoalCreateView,
    GoalUpdateView,
    GoalDeleteView,
)

urlpatterns = [
    # path('', goals_list, name="goals_list"),
    # path('', Goals.as_view(), name="goals_list"),
    path('', GoalsListView.as_view(), name="goals_list"),
    path('detail/<int:pk>/', GoalDetailView.as_view(), name="goal_detail_class"),
    path('create/', GoalCreateView.as_view(), name="goal_create_class"),
    path('update/<int:pk>/', GoalUpdateView.as_view(), name="update_goal_class"),
    path('delete/<int:pk>/', GoalDeleteView.as_view(), name="delete_goal_class"),
    path('update-goal/<int:pk>/', update_goal, name="update_goal"),
    path('delete-goal/<int:pk>/', delete_goal, name="delete_goal"),
]