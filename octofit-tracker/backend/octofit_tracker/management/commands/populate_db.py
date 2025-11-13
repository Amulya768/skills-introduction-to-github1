from django.core.management.base import BaseCommand
from datetime import datetime
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population (using pymongo)...')

        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Collections used by the Django app (approximate names created by Djongo/Django)
        users_col = db['auth_user']
        teams_col = db['octofit_tracker_team']
        activities_col = db['octofit_tracker_activity']
        workouts_col = db['octofit_tracker_workout']
        leaderboard_col = db['octofit_tracker_leaderboardentry']

        # Clear existing data
        activities_col.delete_many({})
        workouts_col.delete_many({})
        leaderboard_col.delete_many({})
        teams_col.delete_many({})
        users_col.delete_many({})

        now_iso = datetime.utcnow()

        # Insert teams
        # Insert teams (provide numeric `id` to satisfy Django/Djongo primary-key expectations)
        teams_col.insert_one({
            'id': 1,
            'name': 'marvel',
            'description': 'Team Marvel',
            'created_at': now_iso
        })
        teams_col.insert_one({
            'id': 2,
            'name': 'dc',
            'description': 'Team DC',
            'created_at': now_iso
        })
        marvel_id = 1
        dc_id = 2

        # Insert users with integer `id` fields to match Django's expected primary key
        users_col.insert_one({
            'id': 1,
            'username': 'ironman',
            'email': 'ironman@example.com',
            'first_name': 'Tony',
            'last_name': 'Stark',
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'date_joined': now_iso,
        })
        users_col.insert_one({
            'id': 2,
            'username': 'spiderman',
            'email': 'spiderman@example.com',
            'first_name': 'Peter',
            'last_name': 'Parker',
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'date_joined': now_iso,
        })
        users_col.insert_one({
            'id': 3,
            'username': 'batman',
            'email': 'batman@example.com',
            'first_name': 'Bruce',
            'last_name': 'Wayne',
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'date_joined': now_iso,
        })
        users_col.insert_one({
            'id': 4,
            'username': 'superman',
            'email': 'superman@example.com',
            'first_name': 'Clark',
            'last_name': 'Kent',
            'is_superuser': False,
            'is_staff': False,
            'is_active': True,
            'date_joined': now_iso,
        })

        # Activities reference users by username/email (not strict FK); include numeric `id`
        activities_col.insert_many([
            {'id': 1, 'user_email': 'ironman@example.com', 'username': 'ironman', 'team_id': marvel_id, 'activity_type': 'run', 'distance': 5.0, 'duration_seconds': 1500, 'timestamp': now_iso},
            {'id': 2, 'user_email': 'spiderman@example.com', 'username': 'spiderman', 'team_id': marvel_id, 'activity_type': 'bike', 'distance': 20.0, 'duration_seconds': 3600, 'timestamp': now_iso},
            {'id': 3, 'user_email': 'batman@example.com', 'username': 'batman', 'team_id': dc_id, 'activity_type': 'run', 'distance': 10.0, 'duration_seconds': 2500, 'timestamp': now_iso},
            {'id': 4, 'user_email': 'superman@example.com', 'username': 'superman', 'team_id': dc_id, 'activity_type': 'other', 'distance': None, 'duration_seconds': 1800, 'timestamp': now_iso},
        ])

        # Workouts (use datetime for date fields and include numeric `id`)
        workouts_col.insert_many([
            {'id': 1, 'user_email': 'ironman@example.com', 'username': 'ironman', 'name': 'Iron Workout', 'description': 'High intensity', 'date': now_iso, 'duration_seconds': 1800},
            {'id': 2, 'user_email': 'batman@example.com', 'username': 'batman', 'name': 'Bat Workout', 'description': 'Stealth training', 'date': now_iso, 'duration_seconds': 2400},
        ])

        # Leaderboard (include numeric `id`)
        leaderboard_col.insert_many([
            {'id': 1, 'user_email': 'ironman@example.com', 'username': 'ironman', 'team_id': marvel_id, 'points': 300, 'rank': 1, 'updated_at': now_iso},
            {'id': 2, 'user_email': 'spiderman@example.com', 'username': 'spiderman', 'team_id': marvel_id, 'points': 200, 'rank': 2, 'updated_at': now_iso},
            {'id': 3, 'user_email': 'batman@example.com', 'username': 'batman', 'team_id': dc_id, 'points': 250, 'rank': 1, 'updated_at': now_iso},
            {'id': 4, 'user_email': 'superman@example.com', 'username': 'superman', 'team_id': dc_id, 'points': 150, 'rank': 2, 'updated_at': now_iso},
        ])

        # Ensure unique index on email for users collection
        try:
            users_col.create_index('email', unique=True)
            self.stdout.write('Created unique index on auth_user.email')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Could not create unique index: {e}'))

        # Summary
        self.stdout.write(self.style.SUCCESS(f'Inserted users: {users_col.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Inserted teams: {teams_col.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Inserted activities: {activities_col.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Inserted workouts: {workouts_col.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Inserted leaderboard entries: {leaderboard_col.count_documents({})}'))
