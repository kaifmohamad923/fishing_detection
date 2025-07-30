from flask import Flask, render_template, request
import joblib
from features import extract_features

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    color = None  # Add color variable

    if request.method == 'POST':
        url = request.form['url']
        features = [extract_features(url)]
        prediction = model.predict(features)[0]
        result = "PHISHING" if prediction == 1 else "LEGITIMATE"
        color = "red" if result == "PHISHING" else "green"

    return render_template('index.html', result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)
