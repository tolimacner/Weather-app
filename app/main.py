import sys
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.weather import fetch_weather

load_dotenv()

api_key = os.getenv('OPENWEATHERMAP_API_KEY')

template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))

app = Flask(__name__, template_folder=template_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="Please enter a city name.")

    weather_data, error_message = fetch_weather(city)
    if weather_data:
        return render_template('index.html', weather=weather_data)
    else:
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
