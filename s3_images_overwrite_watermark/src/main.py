import os
import subprocess
import boto3
from utils import WatermarkImage, ends_with_any

import cv2
import sys
import logging

logging.basicConfig(level=logging.INFO)


s3 = boto3.client('s3')

def elaborate_file_locally(bucket,s3_object_key):
    local_file_name = "./" + s3_object_key.split("/")[-1]
    logging.debug(local_file_name)

    s3.download_file(bucket, s3_object_key, local_file_name)

    cv_image = cv2.imread(local_file_name)

    cv_image = WatermarkImage(cv_image,"./assets/logo.jpeg")

    cv2.imwrite(local_file_name, cv_image)

    with open(local_file_name, 'rb') as f:
        s3.upload_fileobj(f, bucket, s3_object_key)

    os.remove(local_file_name)

    

def main():

    
    src_bucket = os.environ.get('SOURCE_BUCKET')
    folder_name = os.environ.get('FOLDER_NAME', '')
    file_extensions_string = os.environ.get('FILE_EXTENSIONS', 'png,PNG,jpg,jpeg,JPG,JPEG')
    
    file_extensions = file_extensions_string.split(",")
    #additional_line_params = os.environ.get('ADDITIONAL_LINE_PARAMS', '') #for example ' --exclude "*" --include "folder/*" '
    
    paginator = s3.get_paginator('list_objects_v2')

    for page in paginator.paginate(Bucket=src_bucket, Prefix=f"{folder_name}"):
        for obj in page.get('Contents', []):
            key = obj['Key']
            if ends_with_any(key,file_extensions):  # Check if key is within the folder
                logging.debug("analyzing key: " + key)  # Replace with your desired action
                elaborate_file_locally(src_bucket,key)


if __name__ == '__main__':
    main()