pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'
        API_KEY = credentials('OPENWEATHERMAP_API_KEY') // Keep this as your API key is sensitive
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch
                git branch: 'feature/add-weather-feature', url: 'https://github.com/tolimacner/Weather-app.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Test') {
            steps {
                // Set PYTHONPATH and run the tests
                sh 'docker run -e OPENWEATHERMAP_API_KEY=$API_KEY -e PYTHONPATH=/app $DOCKER_IMAGE pytest app/tests/test_weather.py'
            }
        }
    }

    post {
        always {
            // Clean up Docker system (optional)
            sh 'docker system prune -f'
        }
    }
}
