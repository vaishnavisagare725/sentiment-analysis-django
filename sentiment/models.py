from django.db import models
from django.contrib.auth.models import User


class SentimentAnalysis(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    text = models.TextField()

    sentiment = models.CharField(
        max_length=20
    )

    polarity = models.FloatField()

    subjectivity = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.text[:50]