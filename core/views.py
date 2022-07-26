from django.shortcuts import render, redirect

from allauth.account.forms import LoginForm


def landing(request):
    if request.user.is_authenticated:
        return redirect('goals_list')
    form = LoginForm()
    return render(request, 'index.html', {'form': form, 'title': 'goals'})