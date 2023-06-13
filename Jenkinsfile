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
		  def envFile = readFile 'env/version.txt'
		  def envMap = [:]

		  envFile.readLines().each { line ->
		    def (key, value) = line.split('=')
			envMap[key] = value
		  }

		  envMap.each { key, value ->
		    env."$key" = value
			echo "$key=$value"
		  }
		}
	  }
	}

	stage('Check for Version Tag') {
	  steps {
		script {
		  def versionTag = sh (
			script: 'curl -s -S \'https://registry.hub.docker.com/v2/repositories/devkimbob/html_conn/tags/\' | jq \'.\"results\"[][\"name\"]\'',
			returnStdout: true
		  ).trim()

		  echo "$versionTag"

		  if (versionTag.contains("$VERSION")) {
			error("$VERSION tag found. Exiting pipeline.")
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
          sh "kubectl --kubeconfig=/root/admin.yaml get nodes"
		  sh "kubectl --kubeconfig=/root/admin.yaml apply -k kustomize/overlays/prod"
        }
      }
    }
  }
}

