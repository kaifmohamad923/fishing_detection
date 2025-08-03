from sklearn.naive_bayes import MultinomialNB
import pickle
from features import extract_features

# Training data (URLs and labels)
urls = [
    "http://login-facebook.com",
    "https://github.com",
    "http://secure-paypal-login.net",
    "https://www.microsoft.com"
]
labels = [1, 0, 1, 0]  # 1 = phishing, 0 = safe

# Extract features for each URL
X = [extract_features(url) for url in urls]
y = labels

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved using feature-based approach.")
