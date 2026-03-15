from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()
