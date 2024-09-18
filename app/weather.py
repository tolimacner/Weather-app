import os
import requests

# Load the API key from the environment
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

# Define the base URL for the OpenWeatherMap API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    if not API_KEY:
        return None, "API key is missing!"
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors

        data = response.json()

        # Check if city was not found
        if data.get('cod') != 200:
            return None, f"City not found: {city}"

        # Extract relevant weather data
        weather = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather, None

    # Handle different types of exceptions
    except requests.exceptions.HTTPError as http_err:
        return None, f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return None, "Error connecting to the API"
    except requests.exceptions.Timeout:
        return None, "API request timed out"
    except requests.exceptions.RequestException as e:
        return None, f"An error occurred: {e}"
