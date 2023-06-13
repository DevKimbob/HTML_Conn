pipeline {
  agent any

  stages {
    stage('Checkout Source') {
      steps {
        git 'https://github.com/DevKimbob/HTML_Conn.git'
      }
    }

	stage('Set Version') {
	  steps {
	    script {
		  env.VERSION = '1.0.0'
		}
	  }
	}

    stage('Build image') {
      steps {
        script {
          /* sh "export VERSION=${cat version.txt}" */
		  /* sh "export VERSION=1.0.0" */
          sh "docker build -t devkimbob/html_conn:$VERSION ."
          sh "docker tag devkimbob/html_conn:$VERSION devkimbob/html_conn:latest"
        }
      }
    }

    stage('Pushing Image') {
      steps {
        script {
          sh "docker login -u devkimbob -p rlaghwnd135790."
          sh "docker push devkimbob/html_conn:$VERSION"
          sh "docker push devkimbob/html_conn:latest"
        }
      }
    }

    stage('Kubernetes') {
      steps {
        script {
          sh "kubectl --kubeconfig=~/admin.yaml get nodes"
        }
      }
    }
  }
}

