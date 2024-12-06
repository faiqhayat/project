import requests
import pandas as pd
from datetime import datetime

API_KEY = "003f1842ef0697ff6c17016885c4f397"
lon = 73.0479  # Longitude
lat = 33.6844  # Latitude
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

# Function to fetch weather data
def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = [{
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Wind Speed": data["wind"]["speed"],
            "Weather Condition": data["weather"][0]["description"],
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Time": datetime.now().strftime("%H:%M:%S")
        }]
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data, Status Code: {response.status_code}")
        return []

# Save data to CSV
data = fetch_weather_data()
if data:
    df = pd.DataFrame(data)
    df.to_csv("raw_data.csv", index=False)
    print("Weather data saved to raw_data.csv")
else:
    print("No data to save.")
