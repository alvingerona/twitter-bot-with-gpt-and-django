from django.db import models
from django.utils import timezone

class Tweet(models.Model):
    STATUS_PENDING = 0
    STATUS_NOTALLOWED = 1
    STATUS_ALLOWED = 2
    STATUS_CHOICES = [
        (STATUS_PENDING, 'For Review'),
        (STATUS_NOTALLOWED, 'Not allowed to tweet'),
        (STATUS_ALLOWED, 'Allowed to tweet'),
    ]

    body = models.TextField()
    status = models.IntegerField(
        default=STATUS_PENDING, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    tweeted_at = models.DateTimeField(null=True, default=None, help_text="A non-empty value in this field indicates that the tweet has been sent out.")
