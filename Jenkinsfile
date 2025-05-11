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
                echo 'Rulare pylint pe codul raton...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo 'Analiză lib/*.py'
                    pylint --exit-zero lib/*.py || true

                    echo 'Analiză test/*.py'
                    pylint --exit-zero test/*.py || true

                    echo 'Analiză raton.py'
                    pylint --exit-zero raton.py || true
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
                echo "Build Docker pentru raton (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t raton:v${BUILD_NUMBER} .
                    docker rm -f raton${BUILD_NUMBER} || true
                    docker create --name raton${BUILD_NUMBER} -p 8020:5000 raton:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline raton finalizat cu succes.'
        }
        failure {
            echo 'A apărut o eroare în pipeline.'
        }
    }
}


