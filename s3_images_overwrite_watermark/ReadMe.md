# # s3 images overwrite watermark 

This repository contains code and infrastructure to write a watermark on all the images in a bucket or a subfolder using an AWS Fargate task. The bucket names are passed via environment variables. The project is containerized with Docker, and the infrastructure is managed using AWS CloudFormation.

## Project Structure
├── cloudformation/ │ ├── codebuild_ecr_image.yml │ ├── fargate_task.yml ├── src/ │ ├── main.py ├── Dockerfile └── README.md




### Folders

- **src/**: Contains the Python script `main.py`, which is responsible for applying the watermark on the image and overwriting them. The source and destination bucket names are passed through environment variables.
- **cloudformation/**: Contains CloudFormation templates to set up the necessary AWS infrastructure.
  - **codebuild_ecr_image.yml**: A CloudFormation template to create an AWS CodeBuild project that builds the Docker container and pushes it to an AWS ECR repository.
  - **fargate_task.yml**: A CloudFormation template that defines the Fargate task, which can be invoked to run the code. The environment variables (bucket name) are passed to the task at runtime.

### Deploying to AWS with CloudFormation

You can deploy the required infrastructure using the CloudFormation templates.

#### CodeBuild and ECR Setup

1.  Deploy the `codebuild_ecr_image.yml` template to create an AWS CodeBuild project and an ECR repository.
    
    Example command using AWS CLI:

> aws cloudformation deploy \
>       --template-file cloudformation/codebuild-ecr.yml \
>       --stack-name s3-watermark-build \
>       --capabilities CAPABILITY_IAM
#### Fargate Task Setup

1.  Deploy the `fargate_task.yml` template to create the Fargate task definition and associated resources.
    
    Example command using AWS CLI:
  

>   aws cloudformation deploy \   --template-file
> cloudformation/fargate_task.yml \   --stack-name s3-watermark-task \
> --capabilities CAPABILITY_IAM

 2. You can now invoke the Fargate task with the necessary environment variables (source ) to start the process.
 
 ## Environment Variables

-   `SOURCE_BUCKET`: The name of the S3 bucket to replicate from.


These variables are passed to both the Docker container and the Fargate task.