from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal
# Create your views here.

def goals_list(request):

    if request.method == 'POST':
        goal_body = request.POST.get('goal') # check payload and find goal
        Goal.objects.get_or_create(user=request.user, body=goal_body)[0] # make a goal if it doesn't exist
        return redirect('goals_list')
    
    goals = request.user.goals.all()
    return render(request, 'goals/func_goals/goals_list.html', {'goals': goals})

def update_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.body = request.POST.get('goal')
    goal.save()
    return redirect('goals_list')

def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    return redirect('goals_list')
