// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python setup.py build'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
}
