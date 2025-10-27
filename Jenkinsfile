pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Fetching source code from GitHub..."
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/onlyfrontend.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Setting up virtual environment..."
                bat '''
                if not exist venv (
                    python -m venv venv
                )
                call venv\\Scripts\\activate && python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing required dependencies..."
                bat '''
                call venv\\Scripts\\activate
                if exist requirements.txt (
                    pip install -r requirements.txt
                ) else (
                    pip install flask
                )
                '''
            }
        }

        stage('Run Flask App (Background)') {
            steps {
                echo "Starting Flask application in background..."
                bat '''
                start cmd /c "call venv\\Scripts\\activate && python app.py"
                echo Flask app started successfully!
                '''
            }
        }

        stage('Archive Frontend') {
            steps {
                echo "Archiving project files..."
                archiveArtifacts artifacts: '**/*', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}





