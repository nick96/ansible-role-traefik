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
    }
}
