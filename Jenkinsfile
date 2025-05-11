pipeline {
    agent any

    stages {
        stage('Listare directoare') {
            steps {
                sh 'ls -l /home/student/marina/curs_SCC_25_animale'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aplicatie-animale -f /home/student/marina/curs_SCC_25_animale/Dockerfile /home/student/marina/curs_SCC_25_animale'
            }
        }

        stage('Testare') {
            steps {
                dir('/home/student/marina/curs_SCC_25_animale') {
                    sh 'python3 -m app.tests.test_caracteristici'
                }
            }
        }

        stage('Curățare container existent') {
            steps {
                sh 'docker stop animale_container || true'
                sh 'docker rm animale_container || true'
            }
        }

        stage('Rulează Container') {
            steps {
                sh 'docker run -d -p 9090:9090 --name animale_container aplicatie-animale'
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
