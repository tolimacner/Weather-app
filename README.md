# Weather App

This is a simple weather application built with Flask that fetches real-time weather data using the OpenWeatherMap API. The app is containerized using Docker and allows users to search for the current weather in any city.

## Features
- Fetches weather information from the OpenWeatherMap API
- Containerized with Docker for easy deployment
- Simple user interface for entering city names and displaying weather information

## Project Structure

```
weather-app/
├── app/
│   ├── __init__.py        # Marks the app directory as a package
│   ├── main.py            # Flask application code
│   └── weather.py         # Code for fetching weather data from OpenWeatherMap
├── templates/
│   └── index.html         # HTML template for the web interface
├── Dockerfile             # Dockerfile for containerizing the application
├── requirements.txt       # Python dependencies
├── .env                   # Environment file for storing API keys (not included in repository)
└── README.md              # This file
```

## Prerequisites

Before running the application, ensure you have the following installed:
- [Python 3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Set up the `.env` file:

Create a `.env` file in the project root with your OpenWeatherMap API key:

```
OPENWEATHERMAP_API_KEY=your_actual_api_key
```

### 3. Build the Docker image:

```bash
docker build -t weather-app .
```

### 4. Run the Docker container:

```bash
docker run -d -p 5000:5000 --env-file .env weather-app
```

This will run the container on port `5000`. You can access the application in your browser at:

```
http://localhost:5000
```

## Environment Variables

The following environment variables need to be set:
- `OPENWEATHERMAP_API_KEY`: Your OpenWeatherMap API key (you can get it from [OpenWeatherMap](https://openweathermap.org/)).

## Usage

Once the application is running, you can enter a city name in the web interface, and the app will fetch and display the current weather information for that city.

