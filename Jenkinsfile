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
                // Run tests inside the Docker container without removing it after execution
                sh 'docker run -e OPENWEATHERMAP_API_KEY=$API_KEY $DOCKER_IMAGE pytest tests/'
            }
        }
    }

   # post {
        always {
            // Clean up Docker system (you can comment this out temporarily if needed)
            sh 'docker system prune -f'
        }
    }
}

