pipeline {
    agent any

    stages {
        stage('Listare directoare') {
            steps {
                sh 'ls -l /home/student/andrei/curs_SCC_25_animale'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aplicatie-leu -f /home/student/andrei/curs_SCC_25_animale/Dockerfile /home/student/andrei/curs_SCC_25_animale'
            }
        }

        stage('Testare') {
            steps {
                dir('/home/student/andrei/curs_SCC_25_animale') {
                    sh 'python3 -m app.tests.test_caracteristici'
                }
            }
        }

        stage('Curățare container existent') {
            steps {
                sh 'docker stop leut_container || true'
                sh 'docker rm leut_container || true'
            }
        }

        stage('Rulează Container') {
            steps {
                sh 'docker run -d -p 7070:7070 --name leut_container aplicatie-leu'
            }
        }
    }

    post {
        success {
            echo 'Pipeline rulat cu succes!'
        }
        failure {
            echo 'Eroare în pipeline.'
        }
    }
}
