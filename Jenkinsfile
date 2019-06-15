def app = 'Unknown'
pipeline {
    agent any
    stages {
        stage('build'){
            steps{
                script{
                    app = docker.build("dewaniadi/test_jenkins")
                }
            }
        }
    }  
}
