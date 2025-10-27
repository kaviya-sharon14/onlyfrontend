pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Fetching source code from GitHub...'
                deleteDir() // Clean workspace before pulling new code
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/todo-flask-app.git'
            }
        }

        stage('Setup') {
            steps {
                echo '⚙️ Installing dependencies...'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                echo '🚀 Starting Flask app...'
                bat '''
                call venv\\Scripts\\activate
                start /B python app.py
                timeout /t 10
                '''
            }
        }

        stage('Finish') {
            steps {
                echo '✅ Pipeline completed successfully!'
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}








