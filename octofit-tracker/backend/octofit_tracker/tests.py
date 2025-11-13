from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, LeaderboardEntry
from datetime import datetime, date

User = get_user_model()


class BasicModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hero', email='hero@example.com', password='pass')
        self.team = Team.objects.create(name='marvel', description='Marvel team')

    def test_activity_creation(self):
        act = Activity.objects.create(user=self.user, team=self.team, activity_type='run', distance=5.0, duration_seconds=1500, timestamp=datetime.utcnow())
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        w = Workout.objects.create(user=self.user, name='Leg Day', date=date.today(), duration_seconds=3600)
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_entry(self):
        entry = LeaderboardEntry.objects.create(user=self.user, team=self.team, points=100, rank=1)
        self.assertEqual(LeaderboardEntry.objects.first().points, 100)
