pipeline {

    agent any

    environment {
        VENV_DIR = "venv"
        GCP_PROJECT = "omd-emea-adops-kazandirio"
        GCLOUD_PATH ="/var/jenkins_home/google-cloud-sdk/bin"
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
    

    
        stage("Setting up our Virtual Environment and Installing dependencies"){
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

        stage("Building and pushing docker image to GCR"){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')])
                script{
                    echo 'Building and pushing docker image to GCR'
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}

                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                    gcloud config set project ${GCP_PROJECT}

                    gcloud auth configure-docker --quiet

                    docker build -t gcr.io/${GCP_PROJECT}/ml-project:lastest .

                    docker push gcr.io/${GCP_PROJECT}/ml-project:lastest 

                    '''
                }
            }
        }
    }
}