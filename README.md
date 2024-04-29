# Deploy-a-simple-AWS-Lambda-function

Prerequisites

An AWS account with permissions to create Lambda functions, IAM roles, and CloudFormation stacks.
Python installed on your local machine.
An AWS CLI configured with appropriate access credentials.
A GitHub repository to store your Lambda function code.

Steps
1. Clone the Repository
Clone this repository to your local machine

git clone <repository-url>
cd <repository-name>

2 Write the Lambda Function
Open the lambda_function.py file and write your Lambda function code.

3. Define Infrastructure with CloudFormation
Open the cloudformation.yml file and define your Lambda function and IAM role   API Gateway resource

4. Set Up GitHub Secrets
In your GitHub repository, navigate to Settings > Secrets and add the following secrets:

AWS_ACCESS_KEY_ID: Your AWS access key ID.
AWS_SECRET_ACCESS_KEY: Your AWS secret access key.

5. Configure GitHub Actions Workflow
Create a workflow file named .github/workflows/main.yml

6. Deploy Lambda Function
