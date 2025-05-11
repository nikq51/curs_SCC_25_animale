pipeline {
    agent any

    environment {
        IMAGE_NAME = "tigru"
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Preluare cod sursă...'
                checkout scm
            }
        }

        stage('Setup venv și instalare dependințe') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Verificare cod - pylint') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint tigru.py app/lib/*.py app/tests/*.py || true
                '''
            }
        }

        stage('Testare unitară - pytest') {
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

        stage('Rulare Docker (opțional)') {
            steps {
                sh '''
                    docker run -d --name tigru_container_${BUILD_NUMBER} -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo  ' Build + test + dockerizare reușite.'
        }
        failure {
            echo ' A apărut o eroare în pipeline.'
        }
    }
}
