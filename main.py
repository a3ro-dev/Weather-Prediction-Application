import streamlit as st
import numpy as np
import pandas as pd
import time
from modules.weatherModel import WeatherModel

# Function to simulate backend calculations with animated feedback
def perform_calculations(weather_model, num_times, time_of_day, chart, progress_bar, status_text):
    feedback = st.empty()  # Placeholder for feedback messages
    feedback.markdown("### ⏳ Model is starting...")

    messages = [
        "### Looking out in the sky... ☁️",
        "### Checking for any signs of rain... 🌧️",
        "### Solving some algebra... ➗",
        "### Analyzing trends... 📊",
        "### Finalizing predictions... 🔮"
    ]
    for message in messages:
        feedback.markdown(message)
        time.sleep(1)  # Simulating time delay
    
    feedback.markdown("### Predictions ready! 🚀")
    time.sleep(0.5)

    # Fetch predictions from the WeatherModel
    predicted_temps, predicted_weather = weather_model.predict(num_times, time_of_day)

    # Start updating the chart with the predicted data
    for i in range(len(predicted_temps)):
        # Create a DataFrame with predicted values to add to the chart
        new_data = pd.DataFrame({"Temperature": [predicted_temps[i]]})
        chart.add_rows(new_data)  # Add predicted temperature to the chart
        status_text.text(f"{(i+1) * 100 // len(predicted_temps)}% Complete")
        progress_bar.progress((i+1) * 100 // len(predicted_temps))
        time.sleep(0.2)

    progress_bar.empty()
    return predicted_temps, predicted_weather

# Streamlit App
st.set_page_config(page_title="Weather Prediction", page_icon="🌤️", layout="wide")

# Title and Subtitle
st.markdown("<h1 style='text-align: center;'>Weather Prediction Application 🌦️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>A sleek and intuitive UI to predict weather based on past trends</h3>", unsafe_allow_html=True)

# Glassy container for input
st.markdown("""
    <style>
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 1.5em;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        margin-bottom: 2em;
    }
    .stButton > button {
        background-color: #00BFFF;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-size: 1rem;
    }
    .stTextInput {
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Weather types for dropdown selection
weather_options = ["sunny", "cloudy", "rainy", "stormy", "snowy", "windy"]

with st.container():
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### Enter the required inputs below")

    col1, col2 = st.columns(2)

    with col1:
        prev_temps_input = st.text_input("Enter previous temperatures (comma-separated)", value="")
        current_temps_input = st.text_input("Enter current temperatures (comma-separated)", value="")
    
    with col2:
        prev_weather_input = st.multiselect("Select previous weather types", weather_options, default=[])
        current_weather_input = st.multiselect("Select current weather types", weather_options, default=[])

    num_times_input = st.slider("Number of times to predict (e.g., morning, afternoon, evening, night)", min_value=1, max_value=10, value=3)
    time_of_day = st.selectbox("Time of day", ["morning", "afternoon", "evening", "night"])

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Predict"):
        # Input validation
        try:
            prev_temps = list(map(int, prev_temps_input.split(',')))
            current_temps = list(map(int, current_temps_input.split(',')))
    
            if len(prev_temps) != len(current_temps):
                st.error("Temperature lists must be of the same length!")
            elif len(prev_weather_input) != len(current_weather_input):
                st.error("Weather type lists must be of the same length!")
            else:
                weather_model = WeatherModel(prev_temps, current_temps, prev_weather_input, current_weather_input)

                # Initialize chart for progress simulation
                progress_bar = st.sidebar.progress(0)
                status_text = st.sidebar.empty()

                # Create an empty chart with the correct structure
                chart = st.line_chart(pd.DataFrame({"Temperature": []}))

                # Call the perform_calculations function with the new chart logic
                predicted_temps, predicted_weather = perform_calculations(
                    weather_model, num_times_input, time_of_day, chart, progress_bar, status_text
                )
                
                # Display results
                st.success("Prediction Complete! 🎉")
                st.markdown("## Prediction Results")
                
                st.markdown("### Predicted Temperatures")
                for i, temp in enumerate(predicted_temps, 1):
                    st.markdown(f"**Time {i}:** {temp:.2f} °C")
                
                st.markdown("### Predicted Weather Types")
                weather_icons = {"sunny": "☀️", "cloudy": "☁️", "rainy": "🌧️", "stormy": "⛈️", "snowy": "❄️", "windy": "🌬️"}
                predicted_weather_icons = [weather_icons.get(w, "❓") for w in predicted_weather]
                for i, (weather, icon) in enumerate(zip(predicted_weather, predicted_weather_icons), 1):
                    st.markdown(f"**Time {i}:** {icon} {weather.capitalize()}")

        except ValueError:
            st.error("Please ensure temperatures are integers and weather types are strings!")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Created by [a3ro-dev](https://github.com/a3ro-dev) 💻")
