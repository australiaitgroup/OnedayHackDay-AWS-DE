## Requirement:
1. S3 events trigger lambda
2. Save data into DynamoDB

## Steps to Set Up
1. **Python Version**: >=3.8
2. **Environment Variables**: In the Lambda configuration, set up environment variables:
    - `DYNAMO_TABLE`: Name of the table in DynamoDB.
3. **Permissions**: 
    - Ensure the Lambda execution role has `AmazonS3FullAccess`, `AmazonDynamoDBFullAccess` for practice.  
    - However, in reality the least privilege rule needs to be applied.
4. **Create an table in DynamoDB**:
    - Create a table called `customer` with id as partition key
5. **S3 Event Trigger**: Set up an S3 trigger for the Lambda function on the staging bucket. Configure the trigger to fire on `PUT` events.
6. **Timeout**: Increase the Timeout to `60` seconds
7. **Event Template**: Instead of testing lambda by uploading file to S3, `event/event_template.json` can be used to trigger lambda