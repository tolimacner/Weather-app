pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'
        API_KEY = credentials('OPENWEATHERMAP_API_KEY')  // Make sure the Jenkins credential ID is correct
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch
                git url: 'https://github.com/tolimacner/weather-app.git', branch: 'feature-branch'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
    }
}
