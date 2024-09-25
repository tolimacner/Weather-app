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
                // Sleep to keep the container alive for 5 minutes before running the tests
                sh 'docker run -d -e OPENWEATHERMAP_API_KEY=$API_KEY $DOCKER_IMAGE sleep 300 && docker exec $(docker ps -q -f ancestor=$DOCKER_IMAGE) pytest tests/'
            }
        }
    }
}
