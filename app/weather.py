import os
import requests
import logging  # Add this import

logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(location, is_zip=False, country_code=None):
    logging.info(f"Fetching weather for {location}, {country_code}")
    if not API_KEY:
        return None, "API key is missing!"
    
    # Determine the query parameter (either city name or ZIP code)
    if is_zip:
        query = f'{location},{country_code}' if country_code else location
        params = {'zip': query, 'appid': API_KEY, 'units': 'metric'}
    else:
        query = f'{location},{country_code}' if country_code else location
        params = {'q': query, 'appid': API_KEY, 'units': 'metric'}
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        data = response.json()

        # Check if the location was not found
        if data.get('cod') != 200:
            return None, f"Location not found: {location}"

        weather = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather, None
    except requests.exceptions.HTTPError as http_err:
        return None, f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as e:
        return None, f"An error occurred: {e}"
