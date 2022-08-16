pipeline {
    agent any
    stages{
    stage('Build') {
    steps{
         checkout([$class: 'GitSCM', 
                branches: [[name: '*/master']],
                credentialsId:'github_cred',
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: 'CleanCheckout']],
                submoduleCfg: [], 
                userRemoteConfigs: [[url: 'https://github.com/Sannidhi1008/PythonCode.git']]])
              sh "ls -ltr"
        
        echo 'Build done'
        
        }
    
       
    }
     stage('Test') {
            steps {
              checkout([$class: 'GitSCM', 
                branches: [[name: '*/master']],
                credentialsId:'github_cred',
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: 'CleanCheckout']],
                submoduleCfg: [], 
                userRemoteConfigs: [[url: 'https://github.com/Sannidhi1008/PythonCode.git']]])
              sh "ls -ltr"
              echo 'Test done'
          }
        }
    }    
}
