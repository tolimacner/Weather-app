pipeline {
    agent any

    stages {
        stage('List Files') {
            steps {
                sh 'ls -la'
            }
        }
    }

    post {
        always {
            echo '✅ Basic pipeline complete.'
        }
    }
}
