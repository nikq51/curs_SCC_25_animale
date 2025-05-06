pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install') {
      steps { sh 'pip install -r requirements.txt' }
    }
    stage('Test') {
      steps { sh 'pytest --maxfail=1 --disable-warnings -q' }
    }
  }
  post {
    always {
      
    }
  }
}
