# app/main.py
from flask import render_template, request
from app.weather import fetch_weather
from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="Please enter a city name")
    
    data = fetch_weather(city)

    if data.get('cod') != 200:
        return render_template('index.html', error=data.get('message'))

    city_name = data.get('name')
    temp = data.get('main', {}).get('temp')
    description = data.get('weather', [{}])[0].get('description')

    return render_template('index.html', city=city_name, temperature=temp, description=description)

if __name__ == '__main__':
    app.run(debug=True)

