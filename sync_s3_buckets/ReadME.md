# S3 Bucket Replication 

This repository contains code and infrastructure to replicate the contents of one S3 bucket to another using an AWS Fargate task. The bucket names are passed via environment variables. The project is containerized with Docker, and the infrastructure is managed using AWS CloudFormation.

## Project Structure
├── cloudformation/ │ ├── codebuild_ecr_image.yml │ ├── fargate_task.yml ├── src/ │ ├── main.py ├── Dockerfile └── README.md




### Folders

- **src/**: Contains the Python script `main.py`, which is responsible for copying the contents from one S3 bucket to another. The source and destination bucket names are passed through environment variables.
- **cloudformation/**: Contains CloudFormation templates to set up the necessary AWS infrastructure.
  - **codebuild_ecr_image.yml**: A CloudFormation template to create an AWS CodeBuild project that builds the Docker container and pushes it to an AWS ECR repository.
  - **fargate_task.yml**: A CloudFormation template that defines the Fargate task, which can be invoked to replicate the S3 buckets. The environment variables (bucket names) are passed to the task at runtime.

### Deploying to AWS with CloudFormation

You can deploy the required infrastructure using the CloudFormation templates.

#### CodeBuild and ECR Setup

1.  Deploy the `codebuild_ecr_image.yml` template to create an AWS CodeBuild project and an ECR repository.
    
    Example command using AWS CLI:

> aws cloudformation deploy \
>       --template-file cloudformation/codebuild-ecr.yml \
>       --stack-name s3-replication-build \
>       --capabilities CAPABILITY_IAM
#### Fargate Task Setup

1.  Deploy the `fargate_task.yml` template to create the Fargate task definition and associated resources.
    
    Example command using AWS CLI:
  

>   aws cloudformation deploy \   --template-file
> cloudformation/fargate_task.yml \   --stack-name s3-replication-task \
> --capabilities CAPABILITY_IAM

 2. You can now invoke the Fargate task with the necessary environment variables (source and destination S3 buckets) to start the replication process.
 
 ## Environment Variables

-   `SOURCE_BUCKET`: The name of the S3 bucket to replicate from.
-   `DESTINATION_BUCKET`: The name of the S3 bucket to replicate to.

These variables are passed to both the Docker container and the Fargate task.