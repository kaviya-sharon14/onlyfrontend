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

        stage('Install Requirements') {
            steps {
                echo 'Installing dependencies...'
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Flask App in Background') {
            steps {
                echo 'Starting Flask app in background...'
                // Start Flask app without blocking Jenkins
                bat 'start /B cmd /C ".\\venv\\Scripts\\activate && python app.py > flask_log.txt 2>&1"'
                // Wait a few seconds for Flask to start
                bat 'ping -n 5 127.0.0.1 >nul'
                echo 'Flask app is running! ✅'
                echo 'Access it here: http://localhost:5000'
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Archiving frontend files...'
                archiveArtifacts artifacts: '**/*', onlyIfSuccessful: true
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
            echo '🌐 Flask is available at: http://localhost:5000'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}






