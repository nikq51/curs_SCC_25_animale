pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask_app_cal"
        CONTAINER_NAME = "flask_app_cal_container"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Clonare repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Construire imagine Docker...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Pornire container...'
                sh '''
                docker rm -f $CONTAINER_NAME || true
                docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME
                '''
            }
        }

        stage('Testare API') {
            steps {
                echo 'Testare endpoint-uri...'
                sh '''
                sleep 5
                curl -f http://localhost:5000/cal
                curl -f http://localhost:5000/cal/culoare
                curl -f http://localhost:5000/cal/descriere
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizat cu succes!'
        }
        failure {
            echo 'Pipeline eșuat!'
        }
    }
}
