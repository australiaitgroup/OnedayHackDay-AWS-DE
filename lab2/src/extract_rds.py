from asyncio.log import logger
from multiprocessing.reduction import sendfds
import sys
import logging
import pymysql
import os
import pandas as pd
import boto3
from datetime import datetime
import csv

# Define environment variables for the S3 bucket and RDS table name
bucket = os.environ['BUCKET']
table_name = os.environ['TABLE']

# Initialize SSM client to retrieve RDS connection details securely
ssm = boto3.client('ssm')

# Fetch RDS connection parameters from SSM Parameter Store
# Host (RDS endpoint), user, password (decrypted), and database name
host = ssm.get_parameter(Name='/RDS/HOST', WithDecryption=False)['Parameter']['Value']
user = ssm.get_parameter(Name='/RDS/USER', WithDecryption=True)['Parameter']['Value']
password = ssm.get_parameter(Name='/RDS/PASSWORD', WithDecryption=True)['Parameter']['Value']
db_name = ssm.get_parameter(Name='/RDS/DB', WithDecryption=False)['Parameter']['Value']

# Initialize S3 client to upload files
s3_client = boto3.client('s3')

# Attempt to connect to the RDS database
try:
    conn = pymysql.connect(host=host, user=user, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    # Log an error message and exit if connection fails
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()  # Exit if the database connection cannot be established

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded.")

# Lambda function handler
def handler(event, context):
    # SQL statement to select all data from the specified table
    query_stmt = f'SELECT * FROM {table_name};'
    try:
        # Execute SQL query and fetch data
        with conn.cursor() as cur:
            cur.execute(query_stmt)
            rows = cur.fetchall()  # Retrieve all rows from the executed query
            
            # If no data is found, return None
            if not rows:
                return None

            # Convert the query result to a DataFrame
            data = pd.DataFrame(rows)
            # Set DataFrame column names based on SQL query output
            data.columns = [desc[0] for desc in cur.description]
            
            # Generate S3 file path with timestamp
            file_key = 'rds_extraction/' + datetime.now().strftime("%Y/%m/%d/%H/%M/%S") + f'/{table_name}.csv.gz'
            # Define a local file path for the temporary file storage in Lambda
            local_file = '/tmp/' + file_key.replace('/', '-')
            
            # Save the data to a compressed CSV file with non-numeric columns quoted
            data.to_csv(local_file, index=False, encoding='utf-8', compression='gzip', quoting=csv.QUOTE_NONNUMERIC)
            
            # Upload the compressed CSV file to the specified S3 bucket
            upload_file(bucket, file_key, local_file)
    
    except Exception as err:
        # Log an error if data extraction or upload fails
        logger.error(f"ERROR: Unexpected error: Extraction failed when running {query_stmt} in RDS MySQL instance")
        logger.error(err)

# Function to upload a file to S3
def upload_file(bucket, key_name, local_file):
    # Upload the local file to the specified S3 bucket with the given key name
    s3_client.upload_file(local_file, bucket, key_name)
    logger.info(f"SUCCESS: Uploaded {local_file} to {bucket} as {key_name}")
