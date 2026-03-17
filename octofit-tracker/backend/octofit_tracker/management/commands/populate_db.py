
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(username='IronMan', email='ironman@marvel.com'),
            User.objects.create(username='CaptainAmerica', email='captain@marvel.com'),
            User.objects.create(username='Batman', email='batman@dc.com'),
            User.objects.create(username='Superman', email='superman@dc.com'),
        ]

        # Create activities
        Activity.objects.create(user_email='ironman@marvel.com', type='Running', duration=30)
        Activity.objects.create(user_email='captain@marvel.com', type='Cycling', duration=45)
        Activity.objects.create(user_email='batman@dc.com', type='Swimming', duration=60)
        Activity.objects.create(user_email='superman@dc.com', type='Yoga', duration=20)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes')
        Workout.objects.create(name='Power Yoga', description='Yoga for super strength')

        # Create leaderboard
        Leaderboard.objects.create(user_email='ironman@marvel.com', points=100)
        Leaderboard.objects.create(user_email='captain@marvel.com', points=90)
        Leaderboard.objects.create(user_email='batman@dc.com', points=95)
        Leaderboard.objects.create(user_email='superman@dc.com', points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
