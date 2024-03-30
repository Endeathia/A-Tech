pipeline {
    agent any
    
    parameters {
        string(name: 'ROBERTA_IMAGE_URL', defaultValue: '', description: 'Full URL to the Docker image')
    }

    stages {
        stage('Deploy') {
            steps {
                // Deploy to Kubernetes cluster
                script {
                    sh "kubectl apply -f ${ROBERTA_IMAGE_URL}"
                }
            }
        }
    }
}
