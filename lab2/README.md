## Requirement:
1. Extract table from RDS table
2. Save the data into a csv.gz file
3. Upload the csv file into S3 bucket

## Steps to Set Up
1. **Lambda Creation**
    - `Runtime`: python>=3.8
    - `Source Code`: point to the Amazon S3 link URL
    - `Handler`: change handler into extract_rds.handler
2. **Environment Variables**: In the Lambda configuration, set up environment variables:
    - `TABLE`: Name of the source table in RDS.
    - `BUCKET`: Name of the bucket for storing csv file.
3. **Parameters in AWS Systems Manager (SSM) Parameter Store**: Store the RDS connection details in SSM Parameter Store. Go to the SSM Parameter Store console and create the following parameters:
    - `/RDS/HOST`: RDS endpoint (e.g., your-db-instance.abc12345.ap-southeast-1.rds.amazonaws.com)
    - `/RDS/USER`: Database username (enable encryption by choosing SecureString).
    - `/RDS/PASSWORD`: Database password (enable encryption by choosing SecureString).
    - `/RDS/DB`: Database name.
4. **Create an S3 Bucket**:
    - Create an S3 bucket to store the extracted CSV files if you haven’t done so already.
    - Note the bucket name, as it will be used in the Lambda function environment variables.
5. **Permissions**: 
    - Ensure the Lambda execution role has `AmazonS3FullAccess`, `AmazonSSMReadOnlyAccess` for practice.  
    - However, in reality the least privilege rule needs to be applied.
6. **Timeout**: Increase the Timeout to `60` seconds