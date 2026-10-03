from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.analyze_sentiment,
        name="analyze_sentiment"
    ),

    path(
        "history/",
        views.history,
        name="history"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "delete/<int:id>/",
        views.delete_analysis,
        name="delete_analysis"
    ),

    path(
        "api/analyze/",
        views.sentiment_api,
        name="sentiment_api"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]