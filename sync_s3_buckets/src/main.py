import os
import subprocess
import boto3

import sys


def main():

    
    src_bucket = os.environ.get('SOURCE_BUCKET')
    dst_bucket = os.environ.get('DESTINATION_BUCKET')
    additional_line_params = os.environ.get('ADDITIONAL_LINE_PARAMS', '') #for example ' --exclude "*" --include "folder/*" '
    command = f"s3 sync s3://{src_bucket}/ s3://{dst_bucket}/ {additional_line_params}"
    aws_cli_command = f"aws {command} "
    print(aws_cli_command)
    result = subprocess.run(aws_cli_command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    print("syncing terminated")
    
    return result


if __name__ == '__main__':
    main()

