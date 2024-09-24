pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'
        API_KEY = credentials('OPENWEATHERMAP_API_KEY')  // Jenkins credential for API key
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the branch being built
                git branch: 'feature-branch', url: 'https://github.com/tolimacner/weather-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
    }

    post {
        always {
            // Clean up after the build
            sh 'docker system prune -f'
        }
        success {
            echo 'Docker image built successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
