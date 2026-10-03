from django.shortcuts import render, redirect, get_object_or_404

from textblob import TextBlob

from .models import SentimentAnalysis

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# ==========================================
# SENTIMENT CLASSIFICATION FUNCTION
# ==========================================

def classify_sentiment(polarity, subjectivity):

    # Neutral if polarity is very close to zero
    # OR the sentence is mostly objective/factual
    if abs(polarity) <= 0.1 or subjectivity < 0.25:
        return "Neutral"

    elif polarity > 0.1:
        return "Positive"

    elif polarity < -0.1:
        return "Negative"

    else:
        return "Neutral"


# ==========================================
# STEP 29 - SENTIMENT ANALYSIS
# ==========================================

@login_required
def analyze_sentiment(request):

    result = None

    if request.method == "POST":

        text = request.POST.get("text", "").strip()

        if text:

            analysis = TextBlob(text)

            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity

            sentiment = classify_sentiment(
                polarity,
                subjectivity
            )

            SentimentAnalysis.objects.create(
                user=request.user,
                text=text,
                sentiment=sentiment,
                polarity=polarity,
                subjectivity=subjectivity
            )

            result = {
                "text": text,
                "sentiment": sentiment,
                "polarity": polarity,
                "subjectivity": subjectivity
            }

    return render(
        request,
        "sentiment/analyze.html",
        {
            "result": result
        }
    )


# ==========================================
# STEP 30 - USER-SPECIFIC HISTORY
# ==========================================

@login_required
def history(request):

    analyses = SentimentAnalysis.objects.filter(
        user=request.user
    ).order_by("-created_at")

    search = request.GET.get("search")

    sentiment = request.GET.get("sentiment")

    if search:

        analyses = analyses.filter(
            text__icontains=search
        )

    if sentiment:

        analyses = analyses.filter(
            sentiment=sentiment
        )

    return render(
        request,
        "sentiment/history.html",
        {
            "analyses": analyses,
            "search": search,
            "selected_sentiment": sentiment
        }
    )


# ==========================================
# DELETE ANALYSIS
# ==========================================

@login_required
def delete_analysis(request, id):

    analysis = get_object_or_404(
        SentimentAnalysis,
        id=id,
        user=request.user
    )

    analysis.delete()

    return redirect("history")


# ==========================================
# REST API
# ==========================================

@api_view(["POST"])
def sentiment_api(request):

    text = request.data.get("text", "").strip()

    if not text:

        return Response(
            {
                "error": "Text is required"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    subjectivity = analysis.sentiment.subjectivity

    sentiment = classify_sentiment(
        polarity,
        subjectivity
    )

    result = SentimentAnalysis.objects.create(
        text=text,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity
    )

    return Response({

        "id": result.id,

        "text": result.text,

        "sentiment": result.sentiment,

        "polarity": result.polarity,

        "subjectivity": result.subjectivity,

        "created_at": result.created_at
    })


# ==========================================
# STEP 31 - USER-SPECIFIC DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    total = SentimentAnalysis.objects.filter(
        user=request.user
    ).count()

    positive = SentimentAnalysis.objects.filter(
        user=request.user,
        sentiment="Positive"
    ).count()

    negative = SentimentAnalysis.objects.filter(
        user=request.user,
        sentiment="Negative"
    ).count()

    neutral = SentimentAnalysis.objects.filter(
        user=request.user,
        sentiment="Neutral"
    ).count()

    context = {

        "total": total,

        "positive": positive,

        "negative": negative,

        "neutral": neutral,
    }

    return render(
        request,
        "sentiment/dashboard.html",
        context
    )


# ==========================================
# REGISTER
# ==========================================

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        confirm_password = request.POST.get(
            "confirm_password"
        )

        if password != confirm_password:

            return render(
                request,
                "sentiment/register.html",
                {
                    "error": "Passwords do not match"
                }
            )

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "sentiment/register.html",
                {
                    "error": "Username already exists"
                }
            )

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password
        )

        login(request, user)

        return redirect(
            "analyze_sentiment"
        )

    return render(
        request,
        "sentiment/register.html"
    )


# ==========================================
# LOGIN
# ==========================================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(

            request,

            username=username,

            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                "analyze_sentiment"
            )

        return render(

            request,

            "sentiment/login.html",

            {
                "error":
                "Invalid username or password"
            }
        )

    return render(
        request,
        "sentiment/login.html"
    )


# ==========================================
# LOGOUT
# ==========================================

def logout_view(request):

    logout(request)

    return redirect("login")