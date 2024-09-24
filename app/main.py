import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from app.weather import fetch_weather

# Load the .env file to access the API key
load_dotenv()

# Set the template path and Flask app configuration
template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
app = Flask(__name__, template_folder=template_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    zip_code = request.form.get('zip_code')
    country_code = request.form.get('country_code')

    # Check if ZIP code search is used
    if zip_code:
        weather_data, error_message = fetch_weather(zip_code, is_zip=True, country_code=country_code)
    elif city:
        weather_data, error_message = fetch_weather(city, is_zip=False, country_code=country_code)
    else:
        return render_template('index.html', error="Please enter a city or ZIP code.")
    
    if weather_data:
        return render_template('index.html', weather=weather_data)
    else:
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

