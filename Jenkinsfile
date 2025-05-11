pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        // Setează PYTHONPATH la directorul curent ($PWD) și rulează pytest
        sh '''
        python3 -m venv venv 
        . venv/bin/activate
        PYTHONPATH=$PWD pytest --maxfail=1 --disable-warnings -q'''
      }
    }
    stage('Build Docker image') {
      steps {
        sh 'docker build -t lup_app .'
      }
    }
  }
  post {
    always {
      echo 'Pipeline finished (success or failure)'
    }
  }
}
