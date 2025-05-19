import streamlit as st
import pandas as pd
import datetime
from src.sentiment import analyze_sentiment
from src.classifier import predict_stress_level
from src.visualizer import plot_mood_trend

# App Title
st.set_page_config(page_title="MindMate", page_icon="🧠")
st.title("🧠 MindMate - Your AI Mental Health Companion")

# Input Form
with st.form("journal_form"):
    today = datetime.date.today()
    st.subheader(f"Daily Check-in: {today}")
    mood = st.slider("Your Mood (1=Bad, 10=Great)", 1, 10)
    journal = st.text_area("How are you feeling today?")
    submitted = st.form_submit_button("Submit")

if submitted and journal:
    sentiment = analyze_sentiment(journal)
    stress_level = predict_stress_level(journal, mood)

    # Store data
    new_entry = pd.DataFrame({"date": [today], "mood": [mood], "journal": [journal], "sentiment": [sentiment], "stress_level": [stress_level]})
    try:
        data = pd.read_csv("data/user_entries.csv")
        data = pd.concat([data, new_entry], ignore_index=True)
    except FileNotFoundError:
        data = new_entry
    data.to_csv("data/user_entries.csv", index=False)

    st.success(f"Sentiment: {sentiment} | Stress Level: {stress_level}")

    # Recommendations
    st.subheader("🧘 Recommendations")
    if stress_level == "High Stress":
        st.write("- Try guided meditation on Calm or Headspace\n- Go for a short walk\n- Talk to a friend or therapist")
    elif stress_level == "Moderate Stress":
        st.write("- Journaling helps you clarify thoughts\n- Practice deep breathing for 5 minutes")
    else:
        st.write("- Keep doing what you're doing ✨\n- Reflect on your positive habits")

# Visualization
st.subheader("📊 Mood Trend")
try:
    plot_mood_trend("data/user_entries.csv")
except Exception as e:
    st.info("Submit at least one journal entry to view trends.")
