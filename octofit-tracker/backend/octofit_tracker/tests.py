from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        activity = Activity.objects.create(user_email='test@example.com', type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user_email='test@example.com', points=100)
        self.assertEqual(leaderboard.points, 100)
