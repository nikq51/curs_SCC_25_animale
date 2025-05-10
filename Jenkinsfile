pipeline {
    agent any

    parameters {
        booleanParam(name: 'TRIGGER_MANUAL', defaultValue: false, description: 'Rulează manual aplicația Flask?')
    }

    stages {
        stage('Start') {
            steps {
                script {
                    if (params.TRIGGER_MANUAL) {
                        echo "1) Pipeline pornit MANUAL."
                    } else {
                        echo "2) Pipeline pornit AUTOMAT."
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'

            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Se rulează testele unitare...'
                sh 'PYTHONPATH=. ./venv/bin/python -m unittest app.test.test_delfin'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Construiește imaginea Docker...'
                sh 'docker build -t aplicatie-delfin .'
            }
        }

        stage('Cleanup Existing Container') {
            steps {
                echo 'Șterge containerul existent (dacă există)...'
                sh 'docker stop delfin_container || true'
                sh 'docker rm delfin_container || true'
            }
        }

        stage('Run Flask App in Docker (manual only)') {
            when {
                expression { return params.TRIGGER_MANUAL }
            }
            steps {
                echo 'Pornește aplicația Flask în Docker...'
                sh 'docker run -d -p 5000:5000 --name delfin_container aplicatie-delfin'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes.'
        }
        failure {
            echo 'Eroare în pipeline!'
        }
    }
}
