# app/weather.py
import requests

API_KEY = 'b54ab495791eefd72c56b842be753672'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    return response.json()
