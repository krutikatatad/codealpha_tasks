from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# Step 1: Collect FAQs
faq_questions = [
    "What are your working hours?",
    "Where is your office located?",
    "How can I contact support?",
    "What services do you provide?",
    "Do you offer refunds?"
]

faq_answers = [
    "Our working hours are 9 AM to 6 PM, Monday to Friday.",
    "Our office is located in Mumbai, India.",
    "You can contact support at support@example.com.",
    "We provide AI and software development services.",
    "Yes, we offer refunds within 7 days of purchase."
]

# Step 2: Convert text into vectors
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    
    if request.method == "POST":
        user_input = request.form["message"]

        user_vector = vectorizer.transform([user_input])

        similarity = cosine_similarity(user_vector, faq_vectors)

        best_match_index = np.argmax(similarity)

        if similarity[0][best_match_index] > 0.3:
            response = faq_answers[best_match_index]
        else:
            response = "Sorry, I couldn't understand your question."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
