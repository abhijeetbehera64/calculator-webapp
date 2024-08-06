pipeline {
    agent any
    stages {
        stage('Pre-Build') {
            steps {
                script {
                   bat 'mvn clean compile'
                }
            }
        }
       stage ('Build') {
          steps {
             script {
                bat 'mvn -B -DskipTests clean package'
            }
        }
    }
      stage('Test') {
            steps {
                bat 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }         
}
    post {
		script{
		   emailext (
			   body: """
				Hello, Build was successful!!!
				Build ${currentBuild.currentResult}: Job '${env.JOB_NAME}' (${env.BUILD_NUMBER})
				Build URL: ${env.BUILD_URL}
						""",
			   subject: "Build ${currentBuild.currentResult}: Job '${env.JOB_NAME}' (${env.BUILD_NUMBER})",
			   to: 'abhijeetbehera0504@gmail.com',
			   attachLog: true
			   )
	     }
      }
}
