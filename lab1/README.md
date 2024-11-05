## Requirement:
1. Move files between two S3 buckets.
2. Use an event trigger from an S3 bucket (landing bucket) to move the uploaded file to another S3 bucket.
3. Add a timestamp as the key prefix in the destination bucket.
4. Use environment variables for bucket names.

## Steps to Set Up
1. **Python Version**: >=3.8
2. **Environment Variables**: In the Lambda configuration, set up environment variables:
    - `LANDING_BUCKET`: Name of the source bucket (landing bucket).
    - `DESTINATION_BUCKET`: Name of the destination bucket.
3. **S3 Event Trigger**: Set up an S3 trigger for the Lambda function on the landing bucket. Configure the trigger to fire on `PUT` events.
4. **Permissions**: Ensure the Lambda execution role has `s3:GetObject`, `s3:PutObject`, and `s3:DeleteObject` permissions for both buckets.
5. **Timeout**: Increase the Timeout to `30` seconds