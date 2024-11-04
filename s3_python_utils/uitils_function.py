import json
import boto3
import requests


import datetime

s3_client = boto3.client('s3')


def keys(bucket_name, prefix='/', delimiter='/'):
    prefix = prefix[1:] if prefix.startswith(delimiter) else prefix
    bucket = boto3.resource('s3').Bucket(bucket_name)
    return (_.key for _ in bucket.objects.filter(Prefix=prefix))

def checkIfFileExists(s3_client,bucket_name, object_key):
    # Create an S3 client
    
    try:
        # Use the head_object method to check if the object exists and retrieve its metadata
        response = s3_client.head_object(Bucket=bucket_name, Key=object_key)

        return True
        
    except s3_client.exceptions.NoSuchKey:
        # If the object doesn't exist, return False
        return False
    except Exception as e:
        # Handle other exceptions
        #print(e)
        return False  # You can choose to handle the exception differently here if needed 
def returnObjectUploadTime(s3_client,bucket_name, object_key):
    # Create an S3 client
    
    try:
        # Use the head_object method to check if the object exists and retrieve its metadata
        response = s3_client.head_object(Bucket=bucket_name, Key=object_key)

        # If the object exists, get the upload time
        upload_time = response['LastModified']
        return upload_time
    except s3_client.exceptions.NoSuchKey:
        # If the object doesn't exist, return False
        return False
    except Exception as e:
        # Handle other exceptions
        return False  # You can choose to handle the exception differently here if needed
def returnLastUpdatedObjectUploadTime(s3_client,bucket_name, prefix):
    try:
        # Use the list_objects_v2 method to list objects in the folder
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

        # Check if there are any objects in the folder
        if 'Contents' in response:
            # Find the object with the latest upload time
            latest_object = max(response['Contents'], key=lambda x: x['LastModified'])

            # Get the upload time of the latest object
            upload_time = latest_object['LastModified']

            return upload_time
        else:
            return False
    except Exception as e:
        # Handle exceptions
        return False
        
def upload_json_to_s3(s3_client,bucket_name, folder_path, file_name, json_data):
    

    # Combine the folder path and file name to create the object key
    object_key = f'{folder_path}/{file_name}'

    try:
        # Serialize the JSON data to a string
        json_string = json.dumps(json_data)

        # Upload the JSON data to the specified object key in the bucket
        s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=json_string)

        print(f'Successfully uploaded JSON file to s3://{bucket_name}/{object_key}')
    except Exception as e:
        # Handle any exceptions
        print(f'Error uploading JSON file: {str(e)}')