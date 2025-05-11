pipeline {
    agent any

    stages {
        stage('Clonare cod') {
            steps {
                echo ' Codul a fost preluat din repository.'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo ' Se construiește imaginea Docker...'
                sh 'docker build -t aplicatie-animale .'
            }
        }

        stage('Testare') {
            steps {
                echo ' Se rulează testele...'
                sh 'python app/tests/test_caracteristici.py'
            }
        }

        stage('Rulează Container') {
            steps {
                echo ' Se pornește containerul...'
                sh 'docker run -d -p 9090:9090 --name animale_container aplicatie-animale'
            }
        }
    }

    post {
        success {
            echo ' Pipeline finalizat cu succes.'
        }
        failure {
            echo ' A apărut o eroare în pipeline.'
        }
    }
}
