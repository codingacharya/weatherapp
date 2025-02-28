import streamlit as st
import requests

# OpenWeatherMap API Key and URL
API_KEY = "your_api_key_here"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data
def get_weather(city):
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == "404":
        return None
    else:
        main_data = data["main"]
        weather_data = data["weather"][0]
        wind_data = data["wind"]
        
        weather_info = {
            "city": city,
            "temperature": main_data["temp"],
            "pressure": main_data["pressure"],
            "humidity": main_data["humidity"],
            "description": weather_data["description"],
            "wind_speed": wind_data["speed"]
        }
        
        return weather_info

# Streamlit app layout
st.title("Weather Prediction App")

# Input for city name
city = st.text_input("Enter city name:")

if city:
    weather_info = get_weather(city)
    
    if weather_info:
        st.subheader(f"Weather in {weather_info['city']}")
        st.write(f"Temperature: {weather_info['temperature']} °C")
        st.write(f"Pressure: {weather_info['pressure']} hPa")
        st.write(f"Humidity: {weather_info['humidity']} %")
        st.write(f"Weather Description: {weather_info['description']}")
        st.write(f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        st.error(f"City {city} not found. Please check the name and try again.")
