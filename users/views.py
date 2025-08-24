from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('index')
        messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})