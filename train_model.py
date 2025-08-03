import pickle
from features import extract_features
from sklearn.naive_bayes import MultinomialNB

# Training data
urls = [
    "http://login-facebook.com",
    "https://github.com",
    "http://secure-paypal-login.net",
    "https://www.microsoft.com"
]
labels = [1, 0, 1, 0]

# Extract numerical features
X = [extract_features(url) for url in urls]
y = labels

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save only the model (no vectorizer needed)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved successfully.")

