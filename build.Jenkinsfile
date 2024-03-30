pipeline {
    agent any
    stages {
        stage('Docker Login'){
            steps{
                sh 'docker login -u tamer153 -p  Xaydres1998@'
                sh 'Login Successfull'
            }
        }
        stage('Build'){
            steps{
                sh 'docker build -t tamer153/reberta:1.0.0 roberta/.'
                sh 'Build Successful'
            }
        }
        stage('Push the image to Docker Hub'){
            steps{
                sh 'docker push tamer153/reberta:1.0.0 '
            }
        }
    }
}
