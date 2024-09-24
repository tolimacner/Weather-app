pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'
        API_KEY = credentials('OPENWEATHERMAP_API_KEY')  // Fetch the API key from Jenkins credentials
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch code
                git url: 'https://github.com/your-repo/weather-app.git'
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
                // Run the container and pass the API key as an environment variable
                sh '''
                docker run -d --name test-app -p 5000:5000 \
                -e OPENWEATHERMAP_API_KEY=$API_KEY \
                $DOCKER_IMAGE
                sleep 10  # Wait for the app to start
                curl --fail http://localhost:5000 || (echo "Web app test failed"; exit 1)
                '''
            }
        }

        stage('Functionality Test') {
            steps {
                // Simulate entering a city and getting the result
                sh '''
                RESPONSE=$(curl -s -X POST -d "city=London" http://localhost:5000/weather)
                echo $RESPONSE | grep -q "London" || (echo "City result not found in response"; exit 1)
                '''
            }
        }
    }

    post {
        always {
            // Clean up the container
            sh 'docker rm -f test-app || true'
        }
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
