pipeline {
    agent any

    environment {
        VENV_PATH = "./venv"
    }

    stages {
        stage('Build & Setup venv') {
            steps {
                echo 'Setup mediu virtual și instalare dependințe...'
                sh '''
                    python3 -m venv venv
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Pylint - Calitate cod') {
            steps {
                echo 'Rulare pylint pe codul Vulpe...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo 'Analiză lib/*.py'
                    pylint --exit-zero lib/*.py || true

                    echo 'Analiză test/*.py'
                    pylint --exit-zero test/*.py || true

                    echo 'Analiză vulpe.py'
                    pylint --exit-zero vulpe.py || true
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Testare unitară...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    python3 -m unittest discover -s test -p "testare.py"
                '''
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                echo "Build Docker pentru Vulpe (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t vulpe:v${BUILD_NUMBER} .
                    docker rm -f vulpe${BUILD_NUMBER} || true
                    docker create --name vulpe${BUILD_NUMBER} -p 8020:5000 vulpe:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline Vulpe finalizat cu succes.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}


