pipeline {
  agent any
  environment {
      // Using returnStdout
      gitHash = """${sh(
              returnStdout: true,
              script: 'git rev-parse HEAD'
          )}""" 
      dockerRegistry = 'harshaisgud/splitcamelcase'
      dockerHubCredsID = 'ed3c7524-9c90-4b6f-9d04-625f6fe1e59f'
      
  }
  stages {
    stage('Test Application') {
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
    stage('Build Image') {
      steps {
        echo 'Starting to build docker image'

        script {
          sh 'docker build . -f Dockerfile -t $dockerRegistry:$gitHash'
        }
      }
    }
    // stage('Push Image') {
    //   steps {
    //     echo 'Starting to build docker image'

    //     script {
    //       docker.withRegistry('',dockerHubCredsID){
    //           image.push()
    //         }       
    //     }
    //   }
    // }
    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: dockerHubCredsID, passwordVariable: 'password', usernameVariable: 'username')]) {
            sh 'docker login -u $username -p $password'
            sh 'docker push $dockerRegistry:$gitHash'
        }
      }
    }
  }
}

