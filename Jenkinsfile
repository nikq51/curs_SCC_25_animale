pipeline {
    agent any

    environment {
        VENV_PATH = "./.venv-jenkins"
    }

    stages {
        stage('Build & Setup venv') {
            steps {
                echo 'Setup mediu virtual și instalare dependințe...'
                sh '''
                    rm -rf ${VENV_PATH} || true
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    deactivate
                '''
            }
        }

        stage('Pylint - Calitate cod') {
            steps {
                echo 'Rulare pylint pe codul aplicației Animale...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo 'Analiză app/lib/*.py'
                    pylint --exit-zero app/lib/*.py || true
                    echo 'Analiză tests/*.py'
                    pylint --exit-zero tests/*.py || true
                    echo 'Analiză app/Nicolae_441D_Animale.py'
                    pylint --exit-zero app/Nicolae_441D_Animale.py || true
                    deactivate
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Testare unitară...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo "Rulare teste cu Pytest (modul Python)..."
                    python -m pytest
                    deactivate
                '''
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                echo "Build Docker pentru Animale (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t animale-app:v${BUILD_NUMBER} -f ${WORKSPACE}/Dockerfile ${WORKSPACE}
                    docker rm -f animale-container || true
                    docker run -d --name animale-container -p 5001:5001 animale-app:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline Animale finalizat cu succes.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}
