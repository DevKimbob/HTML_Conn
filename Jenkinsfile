pipeline {
  agent any
  stages {
    stage('Checkout Source') {
      steps {
        git 'https://github.com/DevKimbob/HTML_Conn.git'
      }
    }

    stage('Build image') {
      steps {
        script {
		  sh "export VERSION=${cat version.txt}"
		  sh "docker build -t devkimbob/html_conn:${VERSION}"
          sh "docker build -t devkimbob/html_conn:latest ."
        }

      }
    }

    stage('Pushing Image') {
      steps {
        script {
          sh "docker images"
          sh "docker login -u devkimbob -p rlaghwnd135790."
          sh "docker push devkimbob/html_conn:latest"
        }

      }
    }

    stage('Kubernetes') {
      steps {
        echo 'Kubernetes!'
        sh 'pwd'
      }
    }

  }
}
