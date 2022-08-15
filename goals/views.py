from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views import View
from django.views.generic import (
   ListView,
   CreateView,
   UpdateView,
   DeleteView,
   DetailView
)

from .models import Goal
from .forms import SimpleGoalForm, ModelGoalForm
# Create your views here.

@login_required
def goals_list(request):

    if request.method == 'POST':
        form = ModelGoalForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
        # goal_body = request.POST.get('goal') # check payload and find goal
        # Goal.objects.get_or_create(user=request.user, body=goal_body)[0] # make a goal if it doesn't exist
        return redirect('goals_list')
    
    goals = request.user.goals.all()
    create_form = ModelGoalForm()
    edit_form = SimpleGoalForm()
    return render(request, 'goals/func_goals/goals_list.html', {'goals': goals, 'edit_form': edit_form, 'create_form': create_form})

@login_required
@require_POST
def update_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    form = SimpleGoalForm(request.POST)
    
    if goal.user == request.user and form.is_valid():
        goal.body = form.cleaned_data["goal"]
        goal.save()
    return redirect('goals_list')

@login_required
@require_POST
def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if goal.user == request.user:
        goal.delete()
    return redirect('goals_list')


# CBV 

class GoalsListView(LoginRequiredMixin, ListView):
  
   def get_queryset(self):
       queryset = self.request.user.goals.all()
       return queryset

class GoalDetailView(DetailView):
   model = Goal
 
 
class GoalCreateView(CreateView):
   model = Goal
   form_class = ModelGoalForm
   success_url = reverse_lazy('goals_list')
  
   def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)

class GoalUpdateView(UserPassesTestMixin, UpdateView):
   model = Goal
   form_class = ModelGoalForm
   success_url = reverse_lazy('goals_list')
   
   def test_func(self):
    goal = self.get_object()
    if self.request.user == goal.user:
        return True
    return False


class GoalDeleteView(DeleteView):
   model = Goal
   success_url = reverse_lazy('goals_list')