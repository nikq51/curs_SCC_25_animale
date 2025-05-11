pipeline {
    agent any

    stages {
        stage('Listare directoare') {
            steps {
                sh 'tree /home/student/andreea/curs_SCC_25_animale'
            }
        }

        stage('Rulează testele') {
            steps {
                dir('/home/student/andreea/curs_SCC_25_animale') {
                    sh 'python3 app/tests/test_animale.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('/home/student/andreea/curs_SCC_25_animale') {
                    sh 'docker build -t app-panda:latest .'
                }
            }
        }

        stage('Curățare container existent') {
            steps {
                sh 'docker stop app || true'
                sh 'docker rm app || true'
            }
        }

        stage('Rulează containerul') {
            steps {
                sh 'docker run -d -p 5000:5000 --name app app-panda:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline rulat cu succes.'
        }
        failure {
            echo 'Eroare în pipeline.'
        }
    }
}
