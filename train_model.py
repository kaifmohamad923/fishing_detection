from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Training data
X = [
    "http://login-facebook.com",
    "https://github.com",
    "http://secure-paypal-login.net",
    "https://www.microsoft.com"
]
y = [1, 0, 1, 0]

# Feature extraction
vectorizer = CountVectorizer()
X_features = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_features, y)

# Save model and vectorizer using pickle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully.")
