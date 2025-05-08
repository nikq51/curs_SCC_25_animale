pipeline {
    agent any

    parameters {
        booleanParam(name: 'TRIGGER_MANUAL', defaultValue: false, description: 'Rulează manual pipeline-ul?')
    }

    stages {

        stage('Start') {
            steps {
                script {
                    if (params.TRIGGER_MANUAL) {
                        echo "Pipeline pornit MANUAL."
                    } else {
                        echo "Pipeline pornit AUTOMAT."
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r quickrequirements.txt'
            }
        }

        stage('Run Unit Tests from app/test/') {
            steps {
                // Adaugăm app în PYTHONPATH ca să funcționeze importurile din lib
                sh 'PYTHONPATH=app ./venv/bin/python -m unittest app.test.testare'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t tigru-app .'
            }
        }

        stage('Run capibara.py (numai manual)') {
            when {
                expression { return params.TRIGGER_MANUAL }
            }
            steps {
                // Adaugă app/lib în PYTHONPATH pentru ca importurile să funcționeze
                sh 'PYTHONPATH=app ./venv/bin/python capibara.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline terminat cu succes!'
        }
        failure {
            echo 'Eroare în pipeline!'
        }
    }
}

