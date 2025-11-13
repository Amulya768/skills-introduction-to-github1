from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ("run", "Run"),
        ("bike", "Bike"),
        ("swim", "Swim"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="activities")
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    distance = models.FloatField(null=True, blank=True)
    duration_seconds = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.activity_type} @ {self.timestamp}"


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    duration_seconds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.name} ({self.date})"


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leaderboard_entries")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="leaderboard_entries")
    points = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "leaderboard entries"

    def __str__(self):
        return f"{self.user} - {self.points} pts"
