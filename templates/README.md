# 🔍 Phishing URL Detection Tool

A machine learning-based phishing URL detector built using Python, Scikit-learn, and Flask.  
It analyzes URLs and predicts whether they are **phishing** or **legitimate**.

---

## 🚀 Features

- Detects phishing websites using a trained ML model
- Simple web interface (built with Flask)
- Rule-based feature extraction from URLs
- Lightweight and beginner-friendly project

---

## 📦 Tech Stack

- Python 3
- Scikit-learn
- Pandas
- Flask
- Joblib

---

## 📁 Project Structure

phishing_detector/
├── app.py # Flask web app
├── train_model.py # Model training script
├── detector.py # CLI-based detector (optional)
├── features.py # Feature extraction from URLs
├── dataset.csv # Sample phishing + legit URLs
├── model.pkl # Trained ML model
└── templates/
└── index.html # Web UI for user input

yaml
Copy
Edit

---

## 🛠️ How to Run

### ⚙️ Install requirements

```bash
pip install pandas scikit-learn flask joblib
🔄 Train the model
bash
Copy
Edit
python train_model.py
🌐 Start the web app
bash
Copy
Edit
python app.py
Then open your browser and go to:
http://localhost:5000

🧠 How It Works
Extracts features from the URL (length, dots, IPs, symbols, keywords, etc.)

Trained on labeled data using RandomForestClassifier

Predicts 1 = Phishing, 0 = Legitimate

🧪 Sample URLs
Try testing with:

http://login-paypal.account-update.ru → Phishing

https://github.com → Legitimate

## 🧑‍💻 Author

**Shaikh Kaif**  
Red Team & Cybersecurity Enthusiast  
[LinkedIn](https://www.linkedin.com/in/kaifmohamad923/)  
[GitHub](https://github.com/kaifmohamad923)