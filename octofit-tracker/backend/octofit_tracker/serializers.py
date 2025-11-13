from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = ['id', 'name', 'description', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = ['id', 'user', 'team', 'activity_type', 'distance', 'duration_seconds', 'timestamp']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Workout
        fields = ['id', 'user', 'name', 'description', 'date', 'duration_seconds']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeaderboardEntry
        fields = ['id', 'user', 'team', 'points', 'rank', 'updated_at']
