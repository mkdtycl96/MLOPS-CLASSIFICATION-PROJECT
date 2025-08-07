pipeline {

    agent any

    environment {
        VENV_DIR = "venv"
    }

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

    stages{
        stage("Setteing up our Virtual Environment and Installing dependencies"){
            steps{
                script{
                    echo "Cloning Github repo to Jenkins..........."
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}