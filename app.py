from flask import Flask, render_template, request
import pickle
from features import extract_features

app = Flask(__name__)

# Load the model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    color = None
    shadow = None
    if request.method == 'POST':
        url = request.form['url']
        
        # Extract features
        features = extract_features(url)
        
        # Make sure features are passed as a list
        features_vector = vectorizer.transform([features])
        
        # Predict
        prediction = model.predict(features_vector)[0]
        
        # Format result
        result = "PHISHING ❌" if prediction == 1 else "VERIFIED ✅️"
        color = "red" if prediction == 1 else "lime"
        shadow = "#FD0404A0" if prediction == 1 else "#00FF00A4"
        
    return render_template('index.html', result=result, color=color, shadow=shadow)

if __name__ == '__main__':
    app.run(debug=True)

