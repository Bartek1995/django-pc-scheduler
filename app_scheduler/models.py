from django.db import models

class AvailableHours(models.Model):
    day_of_week = models.IntegerField(choices=[
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
