pipeline {
    agent any

    environment {
        IMAGE_NAME = "caine"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Preluare cod...'
                checkout scm
            }
        }

        stage('Setup venv și requirements') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint - pylint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint caine.py app/lib/*.py || true
                '''
            }
        }

        stage('Test - pytest') {
            steps {
                sh '''
                    . .venv/bin/activate
                    PYTHONPATH=. pytest app/tests
                '''
            }
        }

        stage('Build Docker') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Run Docker') {
            steps {
                sh '''
                    docker run -d --name caine_container_${BUILD_NUMBER} -p 5050:5050 ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline reușit!'
        }
        failure {
            echo '❌ A apărut o eroare în pipeline.'
        }
    }
}
