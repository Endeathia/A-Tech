pipeline {
    agent any
    stages {
        stage('Docker Login'){
            steps{
                // Login to Docker Hub
                script {
                    // Log in to Docker Hub
                    sh 'docker login -u tamer153 -p Xaydres1998@'
                    // Check if login was successful
                    if (currentBuild.result == null) {
                        currentBuild.result = 'SUCCESS'
                        echo 'Login Successful'
                    } else {
                        currentBuild.result = 'FAILURE'
                        error 'Docker login failed!'
                    }
                }
            }
        }
        stage('Build'){
            steps{
                // Build Docker image
                script {
                    sh 'docker build -t tamer153/reberta:1.0.0 roberta/.'
                    echo 'Build Successful'
                }
            }
        }
        stage('Push the image to Docker Hub'){
            steps{
                // Push Docker image to Docker Hub
                script {
                    sh 'docker push tamer153/reberta:1.0.0'
                }
            }
        }
    }
}
