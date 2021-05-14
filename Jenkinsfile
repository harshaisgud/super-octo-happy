pipeline {
  agent any
  
  stages {
    stage('Setup') {
      steps {
        sh ' docker build . -t harsha:12344 -f Dockerfile '
      }
    }

  }
}