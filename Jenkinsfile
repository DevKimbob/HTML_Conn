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
		  sh "docker build -t devkimbob/html_conn:latest ."
        }
      }
    }

    stage('Pushing Image') {
      environment {
               registryCredential = 'docker-credential'
           }
      steps{
        script {
		  sh "docker images"
          /* docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) { */
          /*   dockerImage.push("latest") */
          /* } */
        }
      }
    }

    stage('Kubernetes') {
      steps {
		echo "Kubernetes!"
        /* script { */
        /*   kubernetesDeploy(configs: "deployment.yaml", "service.yaml") */
        /* } */
      }
    }

  }

}
