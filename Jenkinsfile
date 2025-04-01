pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tolimacner/weather-app'  // Your Docker image name
        DOCKER_TAG = 'latest'                   // Pull the latest image
        APP_SERVER = 'your-app-server-ip'       // IP address or hostname of your app server
        SSH_USER = 'ubuntu'                     // SSH user for app server
        DOCKER_USERNAME = 'tolimacner'          // DockerHub Username
        DOCKER_PASSWORD = credentials('docker-hub-password')  // DockerHub Password stored in Jenkins
    }

    stages {
        stage('Pull Latest Docker Image') {
            steps {
                script {
                    // Login to DockerHub and pull the latest Docker image
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh "docker pull $DOCKER_IMAGE:$DOCKER_TAG"
                }
            }
        }

        stage('Deploy to App Server') {
            steps {
                script {
                    // Use SSH to connect to the app server and stop the old container, then start the new one
                    sh """
                    ssh -o StrictHostKeyChecking=no $SSH_USER@$APP_SERVER '
                        docker stop weather-app || true
                        docker rm weather-app || true
                        docker pull $DOCKER_IMAGE:$DOCKER_TAG
                        docker run -d --name weather-app -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG
                    '
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                // Optional: Perform a simple check to verify the new version is running
                script {
                    sh """
                    curl http://$APP_SERVER:5000/health || exit 1
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment to production completed successfully.'
        }
        failure {
            echo 'Deployment to production failed!'
        }
    }
}
