from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.conf import settings
from django.core.mail import send_mail
from application.models import Application, Bookmark
from job.models import Job


def send_status_email(application):
    subject = f"Your application for {application.job.title} has been updated"
    message = f"Dear {application.applicant.get_full_name()},\n\n" \
              f"Your application status has been changed to: {application.status}.\n\n" \
              f"Thank you for using our job portal."
    recipient = application.applicant.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])


@login_required
def dashboard_redirect(request):
    user = request.user
    if user.is_recruiter:
        return redirect('recruiter_dashboard')
    else:
        return redirect('candidate_dashboard')


@login_required
def candidate_dashboard(request):
    applications = Application.objects.filter(applicant=request.user).select_related('job')
    return render(request, 'dashboard/candidate_dashboard.html', {'applications': applications})


@login_required
def recruiter_dashboard(request):
    jobs = Job.objects.filter(posted_by=request.user).annotate(app_count=Count('applications'))
    top_jobs = jobs.order_by('-app_count')[:3]
    shortlisted = Application.objects.filter(job__posted_by=request.user, status='Accepted').count()
    declined = Application.objects.filter(job__posted_by=request.user, status='Declined').count()
    total_applications = Application.objects.filter(job__posted_by=request.user).count()

    return render(request, 'dashboard/recruiter_dashboard.html', {
        'top_jobs': top_jobs,
        'shortlisted': shortlisted,
        'declined': declined,
        'total_applications': total_applications,
    })


@login_required
def job_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    query = request.GET.get('q')
    applications = Application.objects.filter(job=job)
    if query:
        applications = applications.filter(applicant__email__icontains=query)
    return render(request, 'dashboard/job_applications.html', {
        'job': job,
        'applications': applications,
        'query': query,
    })


@require_POST
@login_required
def update_application_status(request, app_id, status):
    application = get_object_or_404(Application, id=app_id)
    if application.job.posted_by != request.user:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('job_applications', job_id=application.job.id)

    if status in ['Accepted', 'Declined']:
        application.status = status
        application.is_viewed = True
        application.save()
        send_status_email(application)
        messages.success(request, f"Application status updated to {status}.")
    else:
        messages.error(request, "Invalid status.")

    return redirect('job_applications', job_id=application.job.id)


@login_required
def my_applications(request):
    applications = Application.objects.filter(applicant=request.user).select_related('job')
    return render(request, 'dashboard/my_applications.html', {'applications': applications})


@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('job')
    return render(request, 'dashboard/my_bookmarks.html', {'bookmarks': bookmarks})




# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from application.models import Application,Bookmark 
# from users.models import Recruiter  # assuming custom user roles
# from django.db.models import Q
# from job.models import Job
# from django.contrib import messages
# from django.views.decorators.http import require_POST

# # -----------------------------
# # Candidate Dashboard Views
# # -----------------------------

# @login_required
# def candidate_dashboard(request):
#     applications = Application.objects.filter(applicant=request.user)
#     bookmarks = Bookmark.objects.filter(user=request.user)
#     context = {
#         'total_applications': applications.count(),
#         'total_bookmarks': bookmarks.count(),
#         'recent_applications': applications.order_by('-applied_at')[:5],
#     }
#     return render(request, 'dashboard/candidate_dashboard.html', context)


# @login_required
# def my_applications(request):
#     applications = Application.objects.filter(applicant=request.user).select_related('job')
#     return render(request, 'dashboard/my_applications.html', {'applications': applications})

# @login_required
# def my_bookmarks(request):
#     bookmarks = Bookmark.objects.filter(user=request.user).select_related('job')
#     return render(request, 'dashboard/my_bookmarks.html', {'bookmarks': bookmarks})


# # -----------------------------
# # Recruiter Dashboard View
# # -----------------------------

# @login_required
# def recruiter_dashboard(request):
#     jobs = Job.objects.filter(posted_by=request.user)
#     applications = Application.objects.filter(job__in=jobs)
#     context = {
#         'total_jobs': jobs.count(),
#         'total_applications': applications.count(),
#         'recent_applications': applications.order_by('-applied_at')[:5],
#     }
#     return render(request, 'dashboard/recruiter_dashboard.html', context)


# @login_required
# def job_applications(request, job_id):
#     job = get_object_or_404(Job, id=job_id)
#     if job.posted_by != request.user:
#         messages.error(request, "You are not authorized to view this.")
#         return redirect('home')

#     applications = Application.objects.filter(job=job).select_related('applicant')
#     return render(request, 'dashboard/job_applications.html', {'job': job, 'applications': applications})



# @login_required
# @require_POST
# def update_application_status(request, app_id, status):
#     application = get_object_or_404(Application, id=app_id)
#     if application.job.posted_by != request.user:
#         messages.error(request, "You are not authorized to update this application.")
#         return redirect('home')

#     if status in ['Accepted', 'Declined']:
#         application.status = status
#         application.save()
#         messages.success(request, f"Application marked as {status}.")
#     else:
#         messages.warning(request, "Invalid status.")

#     return redirect('dashboard/job_applications', job_id=application.job.id)

