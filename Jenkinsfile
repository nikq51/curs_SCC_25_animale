pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
          checkout scm 
          }
    }
    stage('Install Dependencies') {
      steps { 
      	   sh 'python3 -m venv venv'
      	   sh 'source venv/bin/activate'
      	   sh './venv/bin/pip install --upgrade pip'
      	   sh './venv/bin/pip install -r requirements.txt'
      	   
      	   }
    }
    stage('Test') {
      steps { 
      	  sh 'cd /home/razvan/SCC/curs_SCC_25_animale'
	  sh 'python3 -m unittest app.test.test_marmota' 
	   
	   }
    }
    stage('Build Docker image'){
       steps {
	  sh 'docker build -t marmota_app .'
	}
    }
  }
  post {
  	success {
            echo 'Succes!'
        }
        failure {
            echo 'Eroare!'
        }
    }
}
