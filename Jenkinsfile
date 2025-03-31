pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/tolimacner/Weather-app.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t tolimacner/weather-app:ver4 .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop weather-app || true
                docker rm weather-app || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name weather-app -p 5000:5000 --env-file .env tolimacner/weather-app:ver4'
            }
        }

        stage('Verify App Running') {
            steps {
                sh 'curl http://localhost:5000 || exit 1'
            }
        }
    }

    post {
        success {
            echo '✅ App deployed and running locally!'
        }
        failure {
            echo '❌ Something went wrong in deployment.'
        }
    }
}
