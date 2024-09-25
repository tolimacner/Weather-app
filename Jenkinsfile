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
                // Run tests inside the Docker container
                sh 'docker run --rm -e OPENWEATHERMAP_API_KEY=$API_KEY $DOCKER_IMAGE pytest tests/'
            }
        }
    }

    post {
        always {
            // Always clean up the Docker images after the job
            sh 'docker system prune -f'
        }
    }
}

