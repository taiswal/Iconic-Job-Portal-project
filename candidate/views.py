from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate
from .forms import CandidateForm
from users.models import User  # Ensure this is your custom user model

# Create candidate profile
def create_candidate_profile(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.user = request.user  # Ensure the user is logged in
            candidate.save()
            return redirect('view_candidate_profile')
    else:
        form = CandidateForm()
    return render(request, 'candidate/candidate_profile.html', {'form': form})


# View candidate profile
def view_candidate_profile(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    return render(request, 'candidate/view_candidate_profile.html', {'candidate': candidate})


# Update candidate profile
def update_candidate_profile(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    if request.method == 'POST':
        form =CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('view_candidate_profile')
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidate/update_candidate_profile.html', {'form': form})


# Delete candidate profile
def delete_candidate_profile(request):
    candidate = get_object_or_404(Candidate, user=request.user)
    if request.method == 'POST':
        candidate.delete()
        return redirect('home')
    return render(request, 'candidate/delete_candidate_profile.html')
