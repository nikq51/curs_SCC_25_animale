pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint check') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pylint koala.py || true
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest app/tests || true
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t koala-app .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker run -d -p 5050:5050 koala-app'
            }
        }
    }
}
