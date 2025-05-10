pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    python3 -m unittest app.test.test_marmota
                '''
            }
        }

        stage('Build Docker image') {
            when {
                expression { fileExists('Dockerfile') }
            }
            steps {
                sh '''
                    docker build -t marmota_app .
                '''
            }
        }
    }

    post {
        failure {
            echo 'Eroare!'
        }
        success {
            echo 'Pipeline rulat cu succes.'
        }
    }
}
