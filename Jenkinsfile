pipeline {
  agent {
    docker {
      image 'python:alpine3.8'
    }

  }
  stages {
    stage('Setup') {
      steps {
        sh ' python3 app_test.py '
      }
    }

  }
}