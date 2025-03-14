pipeline {
    agent any

    environment {
        //AWS_REGION = 'us-east-1'
        S3_BUCKET = 's3-bucket-get-api-data'
        S3_SCRIPT_PATH = 'scripts'
        GLUE_JOB_NAME = 'Get-Api-to-S3-job'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/fatmarekik/terraform-jenkins.git'
            }
        }

        //stage('Install Dependencies') {
        //    steps {
         //       sh 'pip install -r requirements.txt'
          //  }
        //}

        //stage('Run Unit Tests') {
        //    steps {
         //       sh 'pytest tests/'
         //   }
        //}

       stage('Upload Script to S3') {
            steps {
                 withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                  credentialsId: 'aws-jenkins-demo',
                   accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                   secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh '''
                    aws s3 cp glue_job.py s3://$S3_BUCKET/$S3_SCRIPT_PATH/
                    '''
                }
            }
        }

        //stage('Trigger AWS Glue Job') {
        //    steps {
        //        sh '''
        //        aws glue start-job-run --job-name $GLUE_JOB_NAME
         //       '''
          //  }
        //}
    }
}
