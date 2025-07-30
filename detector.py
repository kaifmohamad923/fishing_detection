# detector.py

import joblib
from features import extract_features

# Load the trained model
model = joblib.load("model.pkl")

# Take URL input
url = input("🔍 Enter a URL to check: ")

# Extract features and predict
features = [extract_features(url)]
prediction = model.predict(features)[0]

# Show result
if prediction == 1:
    print("⚠️ Result: PHISHING")
else:
    print("✅ Result: LEGITIMATE")