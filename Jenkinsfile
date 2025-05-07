pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r quickrequirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Important: setăm PYTHONPATH ca să funcționeze importurile
                sh 'PYTHONPATH=. ./venv/bin/python -m unittest discover -s app/tests -p "test_*.py"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t tigru-app .'
            }
        }

    }
}
