pipeline {
  agent any

  environment {
	registry = "devkimbob/html_conn"
	registryCredential = 'docker-credentials'
  }

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
		  dockerImage = docker.build registry + ":$VERSION"
		  echo "$dockerImage"
		  sh "docker tag $registry:$VERSION $registry:latest"
		  taggedImage = dockerImage.tag("latest")
		  echo "$taggedImage"
        }
      }
    }

    stage('Pushing Image') {
      steps {
        script {
		  docker.withRegistry( '', registryCredential ) {
			dockerImage.push()
			sh "docker push $registry:latest"
		  }
        }
      }
    }

	stage('Clean Image') {
	  steps {
		script {
		  sh "docker rmi $registry:$VERSION"
		}
	  }
	}

    stage('Kubernetes') {
      steps {
        script {
          sh "kubectl --kubeconfig=/root/admin.yaml get nodes"
		  sh "kubectl --kubeconfig=/root/admin.yaml apply -k kustomize/overlays/dev"
		  sh "kubectl --kubeconfig=/root/admin.yaml rollout restart -n dev ${kubectl --kubeconfig/root/admin.yaml get deployment -n dev -o name}"
        }
      }
    }
  }
}

