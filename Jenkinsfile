pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'   // Your Docker image name
        DOCKER_TAG = "${env.BUILD_NUMBER}"        // Tag Docker image with build number
        API_KEY = credentials('OPENWEATHERMAP_API_KEY')  // Sensitive API key for tests
        DOCKER_USERNAME = 'your-dockerhub-username'   // DockerHub Username
        DOCKER_PASSWORD = credentials('docker-hub-password')  // DockerHub Password stored as secret in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch from a public repo
                git branch: 'feature/add-weather-feature', url: 'https://github.com/tolimacner/Weather-app.git'
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Test') {
            steps {
                // Run tests inside the Docker container
                sh 'docker run --rm -e OPENWEATHERMAP_API_KEY=$API_KEY $DOCKER_IMAGE:$DOCKER_TAG pytest tests/'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Authenticate and push Docker image
                sh '''
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }

        stage('Create Pull Request') {
            steps {
                script {
                    // Push the branch back to GitHub and create a pull request
                    sh '''
                    git config --global user.email "you@example.com"
                    git config --global user.name "Your Name"
                    git add .
                    git commit -m "Auto-commit from Jenkins"
                    git push origin feature/add-weather-feature
                    gh pr create --title "Auto-generated Pull Request" --body "Pull request created automatically by Jenkins." --base main --head feature/add-weather-feature
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images after the job
            sh 'docker system prune -f'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
