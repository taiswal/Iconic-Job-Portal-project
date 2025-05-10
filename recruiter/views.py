from django.shortcuts import render, redirect, get_object_or_404
from .models import Recruiter
from .forms import RecruiterForm

def create_recruiter_profile(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST, request.FILES)
        if form.is_valid():
            recruiter = form.save(commit=False)
            recruiter.user = request.user  
            recruiter.save()
            return redirect('view_recruiter_profile')
    else:
        form =RecruiterForm()
    return render(request, 'recruiter/create_recruiter_profile.html', {'form': form})

def update_recruiter_profile(request):
    recruiter = get_object_or_404(Recruiter, user=request.user)
    if request.method == 'POST':
        form = RecruiterForm(request.POST, request.FILES, instance=recruiter)
        if form.is_valid():
            form.save()
            return redirect('view_recruiter_profile')
    else:
        form =RecruiterForm(instance=recruiter)
    return render(request, 'recruiter/update_recruiter_profile.html', {'form': form})

def delete_recruiter_profile(request):
    recruiter = get_object_or_404(Recruiter, user=request.user)
    if request.method == 'POST':
        recruiter.delete()
        return redirect('home')
    return render(request, 'recruiter/delete_recruiter_profile.html')

def view_recruiter_profile(request):
    recruiter = get_object_or_404(Recruiter, user=request.user)
    return render(request, 'recruiter/view_recruiter_profile.html', {'recruiter': recruiter})
