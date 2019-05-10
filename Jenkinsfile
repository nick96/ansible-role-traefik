// -*- mode: groovy -*-
pipeline {
    agent {
	docker {
	    image 'quay.io/ansible/molecule:2.20.1'
	}
    }

    stages {
	stage('Test') {
	    steps {
		sh 'molecule test'
	    }
	}

	stage('Tag') {
	    steps {
		script {
		    def meta = readYaml(file: "${workspace}/meta/main.yml")
		    sh "git tag ${meta.version}"
		    sh 'git push --tags'
		}
	    }
	}
    }
}
