"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from django.http import JsonResponse
import os

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')


def codespace_api_root(request, format=None):
    """Return API root using Codespace domain when available (does not modify views.py)."""
    cs = os.environ.get('CODESPACE_NAME')
    if cs:
        base = f"https://{cs}-8000.app.github.dev"
    else:
        # fallback to request host/scheme
        base = request.build_absolute_uri('/').rstrip('/')

    # Return a plain JSON response so Django can serve this view without DRF renderer context
    return JsonResponse({
        'users': f"{base}/api/users/",
        'teams': f"{base}/api/teams/",
        'activities': f"{base}/api/activities/",
        'workouts': f"{base}/api/workouts/",
        'leaderboard': f"{base}/api/leaderboard/",
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', codespace_api_root, name='api-root'),
    path('api/', include(router.urls)),
]
