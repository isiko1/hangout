from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile,
                                user=request.user)
    image = get_object_or_404(UserProfile,)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'image': image
    }

    return render(request, template, context)
