from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registers a new user."""
    if request.method != 'POST':
        # Shows empty register form
        form = UserCreationForm()
    else:
        # Parse filled form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Make login and redirect to main page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Shows empty or incorrect filled form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
