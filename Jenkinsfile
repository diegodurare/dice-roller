pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dduranarellano/dice-roller:jenkins"
        DOCKERHUB_CREDENTIALS_ID = "dockerhub-creds"
    }

    stages {
        stage('Limpiar workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Construir imagen Docker') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage('Test de contenedor') {
            steps {
                script {
                    sh "docker run --name test-container -d $DOCKER_IMAGE"
                    sh "sleep 5"
                    sh "docker logs test-container"
                    sh "docker rm -f test-container"
                }
            }
        }

        stage('Push a DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS_ID) {
                        sh "docker push $DOCKER_IMAGE"
                    }
                }
            }
        }
    }

    post {
        failure {
            echo "El pipeline ha fallado."
        }
    }
}
