from django import forms
from .models import Goal

class SimpleGoalForm(forms.Form):
 goal = forms.CharField(label=False, widget=forms.Textarea(attrs={'class': "form-control"}))


class ModelGoalForm(forms.ModelForm):
    
    class Meta:
        model = Goal
        fields = ('body', )
        labels = {
          'body' : False,
       }
        