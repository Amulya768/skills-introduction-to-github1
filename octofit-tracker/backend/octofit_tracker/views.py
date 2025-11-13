from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework import permissions

from . import models
from . import serializers

User = get_user_model()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.AllowAny]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.ActivitySerializer
    permission_classes = [permissions.AllowAny]


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = models.Workout.objects.all()
    serializer_class = serializers.WorkoutSerializer
    permission_classes = [permissions.AllowAny]


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = models.LeaderboardEntry.objects.all()
    serializer_class = serializers.LeaderboardEntrySerializer
    permission_classes = [permissions.AllowAny]

