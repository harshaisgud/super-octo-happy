pipeline {
  agent any
  environment {
      // Using returnStdout
      gitHash = """${sh(
              returnStdout: true,
              script: 'git rev-parse HEAD | tr -d "\n"'
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
          sh 'docker build . -f Dockerfile --build-arg GITHASH=$gitHash -t $dockerRegistry:$gitHash'
        }
      }
    }
    stage('Push Image') {
      steps {
        echo 'Pushing Image into Registry'
        withCredentials([usernamePassword(credentialsId: dockerHubCredsID, passwordVariable: 'password', usernameVariable: 'username')]) {
            sh 'docker login -u $username -p $password'
            sh 'docker push $dockerRegistry:$gitHash'
        }
      }
    }
    stage('Deploy Application to Minikube') {
      steps {
        echo 'Deploying Application'
        withKubeConfig([credentialsId: 'kubeconfig']) {
          sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.19.0/bin/linux/amd64/kubectl"'  
          sh 'chmod u+x ./kubectl'  
          sh 'sed -i "s|{{version}}|$gitHash|g" ./deployment/deployment.yaml'
          sh './kubectl apply -f ./deployment/deployment.yaml'
        }
      }
    }
    stage('Teardown') {
      steps {
        echo 'Tearing Down Workspace'
        script {
          sh '''
          docker rmi $dockerRegistry:$gitHash
          unset $gitHash
          unset $dockerRegistry
          unset $dockerHubCredsID
          '''
          
        }
      }
    }
  }
}

