pipeline {
  agent {
    docker {
      image 'python:alpine3.8'
    }

  }
  stages {
    stage('Setup') {
      steps {
        sh ' docker build . -t harsha:12344 -f Dockerfile '
      }
    }

  }
}