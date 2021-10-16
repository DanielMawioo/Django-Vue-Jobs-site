from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'userprofiles/dashboard.html', {'userprofile': request.user.userprofile})