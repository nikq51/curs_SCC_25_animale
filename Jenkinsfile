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
                echo 'Rulare pylint pe codul Marmota...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo 'Analiză lib/.py'
                    pylint --exit-zero lib || true

                    echo 'Analiză test/.py'
                    pylint --exit-zero test/.py  true

                    echo 'Analiză marmota.py'
                    pylint --exit-zero capibara.py  true
                '''
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Testare unitară...'
                sh '''
                    . ${VENV_PATH}/bin/activate
                    python3 -m unittest app.test.test_marmota
                '''
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                echo "Build Docker pentru Marmota (ID: ${BUILD_NUMBER})"
                sh '''
                    docker build -t marmota:v${BUILD_NUMBER} .
                    docker rm -f marmota${BUILD_NUMBER}  true
                    docker create --name marmota${BUILD_NUMBER} -p 8020:5000 marmota:v${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'Succes!'
        }
        failure {
            echo 'Eroare!'
        }
    }
}
