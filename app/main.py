from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="Please enter a city name")

    # Fetch weather data
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    data = response.json()

    if data.get('cod') != 200:
        return render_template('index.html', error=data.get('message'))

    # Extract relevant data
    city_name = data.get('name')
    temp = data.get('main', {}).get('temp')
    description = data.get('weather', [{}])[0].get('description')

    return render_template('index.html', city=city_name, temperature=temp, description=description)

if __name__ == '__main__':
    app.run(debug=True)
