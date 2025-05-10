# context_processors.py

from candidate.models import Candidate
from recruiter.models import Recruiter

def user_profile_context(request):
    user = request.user
    profile_data = {}

    if user.is_authenticated:
        try:
            if hasattr(user, 'candidate'):
                profile_data = {
                    'profile_name': user.candidate.full_name,
                    'profile_image': user.candidate.profile_picture.url if user.candidate.profile_picture else None,
                }
            elif hasattr(user, 'recruiter'):
                profile_data = {
                    'profile_name': user.recruiter.full_name,
                    'profile_image': user.recruiter.profile_picture.url if user.recruiter.profile_picture else None,
                }
        except:
            pass

    return {'profile_data': profile_data}
