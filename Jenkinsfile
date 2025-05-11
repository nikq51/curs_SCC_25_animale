pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install') {
      steps { sh '''
apt update
apt install -y python3-pip pyhton3-venv
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
'''}
    }
    stage('Test') {
      steps { sh 'pytest --maxfail=1 --disable-warnings -q' }
    }
    stage('Build Docker image'){
       steps {
sh 'docker build -t alpaca_app .'
	}
    }
  }
  post {
    always {
     echo 'pipeline-ul e gata' 
    }
  }
}
