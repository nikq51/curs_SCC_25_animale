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
                echo 'Rulare pylint pe codul Nevastuica...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo 'Analiză lib/.py'
                    pylint --exit-zero lib || true

                    echo 'Analiză test/.py'
                    pylint --exit-zero test/.py  true

                    echo 'Analiză Nevastuica.py'
                    pylint --exit-zero Nevastuica.py  true
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Testare unitară...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    python3 -m unittest app.test.testare
                '''
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                echo "Build Docker pentru Nevastuica (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t nevastuica:v${BUILD_NUMBER} .
                    docker rm -f nevastuica${BUILD_NUMBER}  true
                    docker create --name nevastuica${BUILD_NUMBER} -p 8020:5000 nevastuica:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline Nevastuica finalizat cu succes.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}
