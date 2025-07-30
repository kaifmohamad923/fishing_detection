from flask import Flask, render_template, request
import joblib
from features import extract_features

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    color = None
    shadow = None
    if request.method == 'POST':
        url = request.form['url']
        features = [extract_features(url)]
        prediction = model.predict(features)[0]
        result = "PHISHING" if prediction == 1 else "LEGITIMATE"
        color = "red" if prediction == 1 else "lime"
        shadow = "#FD0404" if prediction == 1 else "#00FF00"  # ✅ shadow changes too
    return render_template('index.html', result=result, color=color, shadow=shadow)

if __name__ == '__main__':
    app.run(debug=True)
