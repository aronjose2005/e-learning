import pytest
from src.sentiment_analysis import analyze_sentiment

def test_analyze_sentiment():
    feedback = "I love this course!"
    score = analyze_sentiment(feedback)
    assert -1.0 <= score <= 1.0
