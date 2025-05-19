import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

model = joblib.load("model/mental_health_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def preprocess(text):
    text = re.sub(r"[^a-zA-Z ]", "", text.lower())
    return text

def predict_stress_level(text, mood):
    clean_text = preprocess(text)
    X_text = vectorizer.transform([clean_text])
    score = model.predict(X_text)[0] + (10 - mood)
    if score > 15:
        return "High Stress"
    elif score > 10:
        return "Moderate Stress"
    else:
        return "Low Stress"
