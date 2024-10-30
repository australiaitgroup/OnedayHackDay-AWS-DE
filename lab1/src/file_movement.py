import os
import boto3
from datetime import datetime

# Initialize the S3 client
s3 = boto3.client('s3')

# Get bucket names from environment variables
landing_bucket = os.environ['LANDING_BUCKET']
destination_bucket = os.environ['DESTINATION_BUCKET']

def lambda_handler(event, context):
    # Get the object key and bucket from the event
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        # Ensure we're only processing the landing bucket
        if source_bucket != landing_bucket:
            print(f"Skipping object from non-landing bucket: {source_bucket}")
            continue

        # Generate timestamp prefix
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        destination_key = f"{timestamp}/{object_key}"

        try:
            # Copy object to the destination bucket with timestamped key
            s3.copy_object(
                Bucket=destination_bucket,
                CopySource={'Bucket': source_bucket, 'Key': object_key},
                Key=destination_key
            )
            print(f"File copied to {destination_bucket}/{destination_key}")

            # Optionally, delete the file from the source bucket
            # s3.delete_object(Bucket=source_bucket, Key=object_key)
            # print(f"File deleted from {source_bucket}/{object_key}")

        except Exception as e:
            print(f"Error moving file: {e}")
            raise e

    return {
        'statusCode': 200,
        'body': 'File(s) moved successfully'
    }
