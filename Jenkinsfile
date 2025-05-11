pipeline {
    agent any

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    echo "Activare venv și instalare dependențe (etapa Build)..."
                    . ./activeaza_venv
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    echo "Activare venv pentru Pytest..."
                    . ./activeaza_venv;

                    echo "Rulare teste cu Pytest..."
                    pytest; 
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'IN lucru ! ...'
            }
        }
    }
    post {
        always {
            echo 'Pipeline-ul s-a încheiat.'
        }
        success {
            echo 'FELICITĂRI! Pipeline-ul a rulat cu succes!'
        }
        failure {
            echo 'ATENȚIE! Pipeline-ul a eșuat!'
        }
    }
}
