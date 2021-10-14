from django.shortcuts import render
from .models import Job

# Create your views here.
def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'jobs/jobs_details.html', {'job':job})