pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'   // Your Docker image name
        API_KEY = credentials('OPENWEATHERMAP_API_KEY')  // Sensitive API key for tests
        DOCKER_USERNAME = 'tolimacner'   // DockerHub Username
        DOCKER_PASSWORD = credentials('docker-hub-password')  // DockerHub Password stored as secret in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the feature branch
                git branch: 'feature/add-weather-feature', url: 'https://github.com/tolimacner/Weather-app.git'
            }
        }

        stage('Get Latest Docker Version') {
            steps {
                script {
                    // Fetch the latest tag from DockerHub using the v2 API
                    def latestVersion = sh(script: '''
                        curl -s https://hub.docker.com/v2/repositories/tolimacner/weather-app/tags/ | jq -r '.results[].name' | sort -V | tail -n 1
                    ''', returnStdout: true).trim()
                    
                    // Extract the version number and increment it
                    def newVersion = latestVersion.replaceAll('ver', '').toInteger() + 1
                    env.DOCKER_TAG = "ver${newVersion}"
                    
                    echo "New Docker tag: ${env.DOCKER_TAG}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image with the new version tag
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Test') {
            steps {
                // Run tests inside the Docker container
                sh 'docker run --rm -e OPENWEATHERMAP_API_KEY=$API_KEY $DOCKER_IMAGE:$DOCKER_TAG pytest tests/'
            }
        }

        stage('Push Docker Image to DockerHub') {
            steps {
                script {
                    // Login to DockerHub
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'

                    // Push the Docker image
                    sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
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

    post {
        always {
            // Clean up Docker system (optional)
            sh 'docker system prune -f'
        }
    }
}
