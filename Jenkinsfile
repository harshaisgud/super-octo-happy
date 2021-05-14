def commit_id
def app

pipeline {
  agent any
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:alpine3.8'
        }
      }
      steps {
        sh '''
        python3 -m venv env
        source ./env/bin/activate 
        pip install -r requirements.txt
        python3 app_test.py
        ''' 
      }
    }
    stage('build') {
      steps {
        step{
        app = docker.build('harshaisgud/splitcamelcase:$(commit_id)')
        }
      }
    }

  }
}