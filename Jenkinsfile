pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Install Python and dependencies
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python script
                sh '''
                source venv/bin/activate
                python your_script.py
                '''
            }
        }
    }

    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
    }
}