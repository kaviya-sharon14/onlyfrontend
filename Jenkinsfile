pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching source code from public GitHub repo...'
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/todo-flask-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up virtual environment...'
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Flask (if not installed)') {
            steps {
                echo 'Installing Flask if not available...'
                bat '.\\venv\\Scripts\\activate && pip install flask || echo Flask already installed.'
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Starting Flask application...'
                bat '.\\venv\\Scripts\\activate && python app.py'
            }
        }

        stage('Archive Frontend') {
            steps {
                echo 'Archiving static frontend files...'
                archiveArtifacts artifacts: '**/*', onlyIfSuccessful: true
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}



