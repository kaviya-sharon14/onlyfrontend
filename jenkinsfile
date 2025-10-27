pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching source code...'
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/onlyfrontend.git'
            }
        }

        stage('Build') {
            steps {
                echo 'No build needed for static frontend files.'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting local web server...'
                // This command will serve your static files locally
                bat 'python -m http.server 8080'
            }
        }
    }
}
