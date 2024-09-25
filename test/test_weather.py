import os
from app.weather import fetch_weather

def test_fetch_weather():
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    city = "London"
    weather_data, error_message = fetch_weather(city)
    assert weather_data is not None, "Weather data should be returned for valid city"
    assert error_message is None, "There should be no error for valid city"

