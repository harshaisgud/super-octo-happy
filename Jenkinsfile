pipeline {
  agent {
    docker {
      image 'python:alpine3.8'
    }

  }
  stages {
    stage('Setup') {
      steps {
        sh 'pip install -r requirements.txt --user'
      }
    }

  }
}