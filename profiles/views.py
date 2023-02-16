from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def profile(request):
    template = 'profiles/profile.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, template, context)