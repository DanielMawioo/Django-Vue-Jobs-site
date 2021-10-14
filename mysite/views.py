from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from jobs.models import Job


# Create your views here.
def home(request):
    jobs = Job.objects.all()[0:4]
    return render(request, 'mysite/home.html', {'jobs':jobs})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form = UserCreationForm()


    return render(request, 'mysite/signup.html', {'form':form})