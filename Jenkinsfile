pipeline {
    agent any

    environment {
        VENV_PATH = "./venv"
    }

    stages {
        stage('Build & Setup venv') {
            steps {
                echo 'Setup mediu virtual si instalare dependinte...'
                sh '''
                    python3 -m venv venv
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r quickrequirements.txt
                '''
            }
        }

        stage('Pylint - Calitate cod') {
            steps {
                echo 'Rulare analiza statica cu pylint...'
                sh '''
                    . ${VENV_PATH}/bin/activate

                    echo 'Verificare app/lib/*.py'
                    pylint --exit-zero app/lib/*.py || true

                    echo 'Verificare app/test/*.py'
                    pylint --exit-zero app/test/*.py || true

                    echo 'Verificare Vultur.py'
                    pylint --exit-zero Vultur.py || true
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Rulare teste unitare...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    python3 -m unittest discover -s app/test -p "testare.py"
                '''
            }
        }

        stage('Docker Build & Run') {
            steps {
                echo "Build si lansare container Docker - ID: ${BUILD_NUMBER}"
                sh '''
                    docker build -t vultur:v${BUILD_NUMBER} .

                    echo 'Stergere container anterior daca exista...'
                    docker rm -f vultur${BUILD_NUMBER} || true

                    echo 'Pornire nou container...'
                    docker run -d --name vultur${BUILD_NUMBER} -p 8020:5000 vultur:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes.'
        }
        failure {
            echo 'A aparut o eroare in pipeline.'
        }
    }
}

