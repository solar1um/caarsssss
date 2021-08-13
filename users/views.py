from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import ProfileRegistrationForm


def register(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = ProfileRegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST, request.FILES,
                                       instance=request.user)
        context = {
            'form': form
        }
        return render(request, 'users/profile.html',
                      context)


