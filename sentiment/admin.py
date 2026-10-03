
from django.contrib import admin
from .models import SentimentAnalysis


@admin.register(SentimentAnalysis)
class SentimentAnalysisAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "sentiment",
        "polarity",
        "subjectivity",
        "created_at"
    )

    list_filter = ("sentiment",)

    search_fields = ("text",)
