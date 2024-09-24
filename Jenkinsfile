pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'
        API_KEY = credentials('OPENWEATHERMAP_API_KEY') // Keep this as your API key is sensitive
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch, no credentials needed for public repo
                git branch: 'feature/add-weather-feature', url: 'https://github.com/tolimacner/Weather-app.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        // Additional stages as needed...
    }
}
