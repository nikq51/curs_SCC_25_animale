pipeline {
agent any

environment {
PYTHONPATH = "${env.WORKSPACE}"
}

stages {
stage('Install dependencies'){
steps{
sh 'python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt'
}
}

stage ('Lint'){
steps{
sh '.venv/bin/pylint lemur.py || true'
}
}

stage('Docker Build'){
steps {
sh 'docker build -t lemur-app .'
}
}

stage ('Docker Run'){
steps{
sh 'docker run -d -p 5050:5050 lemur-app'
}
}
}


