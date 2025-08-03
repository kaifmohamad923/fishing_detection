from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load pipeline (vectorizer + classifier)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    color = None
    shadow = None
    if request.method == 'POST':
        url = request.form['url']
        prediction = model.predict([url])[0]
        result = "PHISHING ❌" if prediction == 1 else "VERIFIED ✅️"
        color = "red" if prediction == 1 else "lime"
        shadow = "#FD0404A0" if prediction == 1 else "#00FF00A4"
    return render_template('index.html', result=result, color=color, shadow=shadow)

if __name__ == '__main__':
    app.run(debug=True)

