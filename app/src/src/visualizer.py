import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_mood_trend(csv_path):
    df = pd.read_csv(csv_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values("date")

    fig, ax = plt.subplots()
    ax.plot(df['date'], df['mood'], marker='o', linestyle='-')
    ax.set_title("Mood Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Mood (1-10)")
    st.pyplot(fig)
