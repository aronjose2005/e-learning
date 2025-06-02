from e_learning import generate_learning_content
from quantum_processing import process_data_efficiently
from sentiment_analysis import analyze_sentiment

def main():
    # Sample student feedback
    student_feedback = "I find math difficult but I enjoy science."
    print(f"Student Feedback: {student_feedback}")

    # Analyze sentiment
    sentiment_score = analyze_sentiment(student_feedback)
    print(f"Sentiment Score: {sentiment_score}")

    # Quantum-enhanced processing
    processed_data = process_data_efficiently(student_feedback)
    print(f"Quantum-Enhanced Processed Data: {processed_data}")

    # Generate personalized learning content
    content = generate_learning_content(student_feedback, sentiment_score)
    print(f"Personalized Learning Content: {content}")

if __name__ == "__main__":
    main()
