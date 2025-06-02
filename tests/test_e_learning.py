import pytest
from src.e_learning import generate_learning_content

def test_generate_learning_content():
    feedback = "I struggle with math."
    sentiment_score = 0.5
    content = generate_learning_content(feedback, sentiment_score)
    assert isinstance(content, str)
    assert len(content) > 0
