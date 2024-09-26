pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'
<<<<<<< HEAD
        API_KEY = credentials('OPENWEATHERMAP_API_KEY') // Keep this as your API key is sensitive
=======
        API_KEY = credentials('OPENWEATHERMAP_API_KEY')  // Make sure the Jenkins credential ID is correct
>>>>>>> main
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch
<<<<<<< HEAD
                git branch: 'feature/add-weather-feature', url: 'https://github.com/tolimacner/Weather-app.git'
=======
                git url: 'https://github.com/tolimacner/weather-app.git', branch: 'feature-branch'
>>>>>>> main
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
<<<<<<< HEAD

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
=======
>>>>>>> main
    }
}
