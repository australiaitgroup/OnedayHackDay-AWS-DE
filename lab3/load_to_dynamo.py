import json 
import boto3
import csv
import uuid
import gzip
from datetime import datetime
import os

# Initializing the S3 resource using boto3
s3 = boto3.resource('s3')
# Defining a local file path to temporarily store the downloaded CSV file
local_file = '/tmp/data.csv.gz'  # Updated to reflect .csv.gz file
# Initializing the DynamoDB resource using boto3
dynamodb = boto3.resource('dynamodb')
# Accessing the DynamoDB table specified in the Lambda environment variable 'DYNAMO_TABLE'
table = dynamodb.Table(os.environ['DYNAMO_TABLE'])
# Getting the current date in "YYYY-MM-DD" format to include in the DynamoDB item
date = datetime.now().strftime("%Y-%m-%d")

# Lambda function handler that is triggered by an S3 event (when a file is uploaded to S3)
def lambda_handler(event, context):
    # Extracting the records (files) from the event that triggered this Lambda
    records = event['Records']
    
    # Looping through each record (each uploaded file)
    for record in records:
        # Retrieving the name of the S3 bucket where the file is stored
        bucket = record['s3']['bucket']['name']
        # Retrieving the key (path) of the file in the S3 bucket
        key = record['s3']['object']['key']
        
        # Calling the process_data function to download and process the S3 file
        process_data(bucket, key, local_file)

# Function to process the CSV data from S3 and store it in DynamoDB
def process_data(bucket, key, file):
    # Downloading the CSV.GZ file from S3 to the local /tmp directory
    s3get(bucket, key, file)
    
    # Opening the downloaded .csv.gz file in read mode
    with gzip.open(file, mode='rt') as gz_file:  # Using gzip.open to read the gzipped file
        # Reading the CSV file using DictReader, which reads the file as a dictionary
        csv_reader = csv.DictReader(gz_file)
        
        # Looping through each row in the CSV file
        for row in csv_reader:
            # Converting each row (a dictionary) to a JSON string
            row_json = json.dumps(row)
            
            # Printing the JSON string to the Lambda logs (for debugging purposes)
            print(row_json)
            
            # Generating a unique ID for each row using UUID
            id = str(uuid.uuid4())
            
            # Inserting the row data as an item into the DynamoDB table
            table.put_item(
                Item = {
                    'id': id,  # Unique ID for each entry
                    'date': date,  # The current date (formatted as YYYY-MM-DD)
                    'content': row_json  # The CSV row content as a JSON string
                }
            )

# Function to download the CSV.GZ file from an S3 bucket to a local file path
def s3get(bucket, key, file):
    # Using boto3 to download the S3 object (file) to the local file path
    s3.Object(bucket, key).download_file(file)
