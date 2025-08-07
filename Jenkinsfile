pipeline {

    agent any

    stages{
        stage("Cloning Github repo to jenkins"){
            steps{
                script{
                    echo "Cloning Github repo to Jenkins..........."
                    checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/mkdtycl96/MLOPS-CLASSIFICATION-PROJECT.git']])
                }
            }
        }
    }
}