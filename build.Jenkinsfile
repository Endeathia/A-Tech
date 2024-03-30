pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = 'tamer153/roberta' // My docker Hub
        IMAGE_TAG = "${DOCKER_HUB_REPO}:${BUILD_NUMBER}" // TAG the IMAGE
    }
    stages{
        stage('Docker Login'){
            steps{
                script{
                    withCredentials([usernamePassword(credentialsId: 'DockerHub1', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'USER_NAME')]) {
                        sh 'docker login -u ${USER_NAME} -p ${DOCKER_PASSWORD} '
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
        }
        stage('Docker Build'){
            steps{
                script{
                    sh "docker build -t ${IMAGE_TAG} roberta/." // Build The Image
                }
            }
        }
        stage('Docker Push'){
            steps{
                script{
                    sh "docker push ${IMAGE_TAG}"
                }
            }
        }
    }
}