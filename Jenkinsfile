pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching source code...'
                git branch: 'main', url: 'https://github.com/kaviya-sharon14/todo-flask-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up virtual environment...'
                bat """
                if exist %VENV_DIR% rmdir /S /Q %VENV_DIR%
                python -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                python -m pip install --upgrade pip
                """
            }
        }

        stage('Install Flask (if not installed)') {
            steps {
                echo 'Installing Flask if missing...'
                bat """
                call %VENV_DIR%\\Scripts\\activate
                python -m pip install flask || echo Flask already installed
                """
            }
        }

        stage('Run Flask App') {
            steps {
                echo 'Starting Flask application...'
                bat """
                call %VENV_DIR%\\Scripts\\activate
                python app.py
                """
            }
        }

        stage('Archive Frontend') {
            steps {
                echo 'Archiving frontend files (index.html, CSS, JS)...'
                archiveArtifacts artifacts: '**/*.html, **/*.css, **/*.js', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo '✅ Flask + Frontend pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
        always {
            bat 'if exist %VENV_DIR% rmdir /S /Q %VENV_DIR%'
        }
    }
}


