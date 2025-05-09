pipeline {
    agent any

    environment {
        IMAGE_NAME = "puma"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Clonare cod') {
            steps {
                echo "Se clonează repository-ul..."
                checkout scm
            }
        }

        stage('Pregătire mediu și instalare') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Linting (pylint)') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint puma.py app/lib/*.py || true
                '''
            }
        }

        stage('Testare unitară (pytest)') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest app/tests
                '''
            }
        }

        stage('Build imagine Docker') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Rulare container Docker') {
            steps {
                sh '''
                    docker run -d --rm --name puma_${BUILD_NUMBER} -p 5001:5001 ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completat cu succes."
        }
        failure {
            echo "A apărut o eroare în timpul execuției pipeline-ului."
        }
    }
}
