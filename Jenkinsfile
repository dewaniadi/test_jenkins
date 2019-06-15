pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'docker build -t dewaniadi/test_jenkins:${BUILD_NUMBER} -f Dockerfile .'
                sh 'docker push dewaniadi/test_jenkins:${BUILD_NUMBER}'
            }
        }
    }
}
