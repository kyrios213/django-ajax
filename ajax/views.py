from django.shortcuts import render
from django.http import JsonResponse

from .models import Profile

def index(request):
    return render(request, 'index.html', {})


def getProfiles(request):
    profiles = Profile.objects.all()

    return JsonResponse({'profiles': list(profiles.values())})