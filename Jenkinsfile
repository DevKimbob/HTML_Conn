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
		  def envFile = readFile 'version.txt'
		  def envMap = [:]

		  envFile.readLines().each { line ->
		    def (key, value) = line.split('=')
			envMap[key] = value
		  }

		  envMap.each { key, value ->
		    env."$key" = value
		  }
		}
	  }
	}

    stage('Build image') {
      steps {
        script {
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

