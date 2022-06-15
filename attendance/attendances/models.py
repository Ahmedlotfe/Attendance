from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta



class Attendance(models.Model):
    status_choices = [
        ('check_in', 'check_in'),
        ('check_out', 'check_out'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=status_choices)
    duration = models.DurationField(default=timedelta())

    def __str__(self):
        return self.user.username
