from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Perform any processing needed
            return redirect('register')  # Redirect to another page on success
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def regi(request):
    return render(request, 'register1.html')
