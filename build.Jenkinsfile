pipline {
    agent any
    stages {
        stage('Build'){
            steps{
                sh 'docker login -u tamer153 -p  Xaydres1998@'
                sh 'docker build -t tamer153/roberta:1.0.0 roberta/.'
                sh 'docker push tamer153/reoberta:1.0.0'
            }
        }
    }
}
