/*Jenkins*/
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
                    . ./activeaza_venv
                    '''
            }
        }
        
        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    echo "Activare venv pentru Pylint..."
                    source ./activeaza_venv; 

                    echo '\n\nVerificare app/lib/*.py cu pylint\n'; 
                    pylint --exit-zero app/lib/*.py;

                    echo '\n\nVerificare tests/*.py cu pylint';    
                    pylint --exit-zero tests/*.py;

                    echo '\n\nVerificare app/Nicolae_441D_Animale.py cu pylint'; 
                    pylint --exit-zero app/Nicolae_441D_Animale.py; 
                '''
            }
        }

        stage('Unit Testing cu pytest') { 
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    echo "Activare venv pentru Pytest..."
                    source ./activeaza_venv;

                    echo "Rulare teste cu Pytest..."
                    pytest; 
                '''
            }
        }

        stage('Deploy') { 
            agent any
            steps {
                echo 'IN lucru ! ...' // Placeholder
                //Docker build și run/push din etapa de containerizare
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
