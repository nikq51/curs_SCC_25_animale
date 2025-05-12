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
        sh 'PYTHONPATH=$PWD pytest --maxfail=1 --disable-warnings -q'
      }
    }
    stage('Build Docker image') {
      steps {
        sh 'docker build -t veverita_app .'
      }
    }
    stage('Run Docker image') {
      steps {
    // Oprește și șterge eventualul container existent cu același nume
        sh '''
          docker rm -f veverita_container || true
          docker run -d -p 5000:5000 --name veverita_container veverita_app
          '''
      }
    }

  }
  post {
    always {
      echo 'Pipeline finished (success or failure)'
    }
  }
}
