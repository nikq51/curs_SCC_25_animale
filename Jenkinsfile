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
                    sh 'python3 -m app.tests.test_animale'
                }
            }
        }

        stage('Build Docker Image pentru aplicatie') {
            steps {
                sh 'docker build -t app-panda -f /home/student/andreea/curs_SCC_25_animale/Dockerfile /home/student/andreea/curs_SCC_25_animale'
            }
        }

        stage('Curățare container existent, in cazul in care a mai fost rulat pipelineul') {
            steps {
                sh 'docker stop app || true'
                sh 'docker rm app || true'
            }
        }

        stage('Rulează Container app') {
            steps {
                sh 'docker run -d -p 5000:5000 --name app app-panda'
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
