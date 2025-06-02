from transformers import pipeline

# Analyze sentiment of student feedback using NLP
def analyze_sentiment(feedback_text):
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analyzer(feedback_text)[0]
    score = result["score"] if result["label"] == "POSITIVE" else -result["score"]
    return score
