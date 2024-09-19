import os
import requests


API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
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
        
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  

        data = response.json()

        
        if data.get('cod') != 200:
            return None, f"City not found: {city}"

        
        weather = {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather, None

    
    except requests.exceptions.HTTPError as http_err:
        return None, f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return None, "Error connecting to the API"
    except requests.exceptions.Timeout:
        return None, "API request timed out"
    except requests.exceptions.RequestException as e:
        return None, f"An error occurred: {e}"
