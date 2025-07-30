import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
from sklearn.model_selection import train_test_split

from features import extract_features

# 1 load dataset
df = pd.read_csv("dataset.csv")

# 2. Extract features and labels
X = df['url'].apply(extract_features).tolist()
y = df['label'].map({'legitimate': 0, 'phishing': 1})  # Convert to 0 and 1

# 3. Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# 6. Save model
joblib.dump(model, "model.pkl")
print("💾 Model saved as model.pkl")