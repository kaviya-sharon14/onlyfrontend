pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Fetching source code from public GitHub repo...'
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/todo-flask-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Flask (if not installed)') {
            steps {
                echo '📦 Installing Flask (if missing)...'
                bat '.\\venv\\Scripts\\activate && pip install flask || echo Flask already installed.'
            }
        }

        stage('Run Flask App in Background') {
            steps {
                echo '🚀 Launching Flask app in background...'
                bat 'start /B cmd /C ".\\venv\\Scripts\\activate && python app.py > flask_log.txt 2>&1"'
                echo '🌐 Flask app running at: http://localhost:5000'
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo '🗂️ Archiving project files...'
                archiveArtifacts artifacts: '**/*', onlyIfSuccessful: true
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
            echo '-----------------------------------------'
            echo '🌍 Access your app here: http://localhost:5000'
            echo '-----------------------------------------'
        }
        failure {
            echo '❌ Pipeline failed. Check error logs.'
        }
    }
}







