from django.shortcuts import get_object_or_404, render, redirect
from .models import Goal
# Create your views here.


def goals_list(request):
    goals = request.user.goals.all()
    
    if request.method == "POST":
        goal = request.POST.get('goal')
        Goal.objects.get_or_create(user=request.user, body=goal)[0]
        return redirect('goals_list')


    return render(request, 'goals/func_goals/goals_list.html', {'goals': goals})


def update_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    
    if request.method == "POST":
        goal.body = request.POST.get('goal')
        goal.save()
        return redirect('goals_list')
    
    return render(request, 'goals/func_goals/update_goal.html', {'goal': goal})


def delete_goal(request, pk):
   goal = get_object_or_404(Goal, pk=pk)
 
   if request.method == 'POST':
       goal.delete()
       return redirect('goals_list')
 
   return render(request, 'goals/func_goals/delete_goal.html', {'goal': goal})
