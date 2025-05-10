from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application, Bookmark
from job.models import Job
from .forms import ApplicationForm
from django.views.decorators.http import require_POST

from django.conf import settings

@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, "You have already applied to this job.")
        return redirect('job_detail', job_id=job.id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, "Application submitted successfully.")
            return redirect('job_detail', job_id=job.id)
    else:
        form = ApplicationForm()
    
    return render(request, 'application/apply.html', {'form': form, 'job': job})

@login_required
def bookmark_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, job=job)
    if not created:
        messages.info(request, "You already bookmarked this job.")
    else:
        messages.success(request, "Job bookmarked.")
    return redirect('job_detail', job_id=job.id)

# @require_POST
# @login_required
# def update_application_status(request, app_id, status):
#     application = get_object_or_404(Application, id=app_id)

#     # Only the recruiter who posted the job can update
#     if application.job.posted_by != request.user:
#         messages.error(request, "You are not authorized to perform this action.")
#         return redirect('job_applications', job_id=application.job.id)

#     if status in ['Accepted', 'Declined']:
#         application.status = status
#         application.is_viewed = True
#         application.save()

#         send_status_email(application)  

#         messages.success(request, f"Application status updated to {status}.")
#     else:
#         messages.error(request, "Invalid status.")

#     return redirect('job_applications', job_id=application.job.id)
