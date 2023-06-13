pipeline {

  environment {
    dockerimagename = "devkimbob/html-conn"
    dockerImage = ""
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git 'https://github.com/DevKimbob/HTML_Conn.git'
      }
    }

    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build dockerimagename
        }
      }
    }

    stage('Pushing Image') {
      environment {
               registryCredential = 'docker-credential'
           }
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Kubernetes') {
      /* steps { */
      /*   script { */
      /*     kubernetesDeploy(configs: "deployment.yaml", "service.yaml") */
      /*   } */
      }
    }

  }

}
