pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Fetching static frontend files from GitHub...'
                deleteDir() // clean workspace
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/onlyfrontend.git'
            }
        }

        stage('Publish Frontend') {
            steps {
                echo '🚀 Copying frontend files to Jenkins public directory...'
                // Copy all static files into Jenkins userContent directory
                bat '''
                xcopy * "%JENKINS_HOME%\\userContent" /E /Y
                '''
            }
        }

        stage('Finish') {
            steps {
                echo '✅ Frontend published successfully!'
                echo '🌍 Open your frontend in browser:'
                echo '👉 http://localhost:8080/userContent/'
            }
        }
    }

    post {
        failure {
            echo '❌ Deployment failed. Please check logs.'
        }
    }
}
