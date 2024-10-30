# OnedayHackDay-AWS-DE

## Pre-requisite
1. Make sure Terminal is available on your laptop (Mac or WSL on Windows)
2. New AWS account is created

## Content
#### Build a data pipeline on AWS including the following steps:
1. Read data from Database(Mysql in RDS)
2. Save data as csv file in S3 bucket
3. Use S3 event trigger to kick off lambda
4. Use lambda to transfer the data format and load into NoSQL database(DynamoDB) 

## Schedule
- 10:30 - 10:45
    - Ice-Break & Introduction
- 10:45 - 11:40 Section 1
    - AWS Overview about Data Engineering
    - IAM, S3 Overview
    - Create S3 Bucket through AWS Console
- 11:40 - 11:50 Morning Break 
- 11:50 - 12:50 Section 2
    - Lambda Overview
    - Lab 1: Lambda - S3 event trigger
- 12:50 - 13:50 Lunch Break & Networking
- 13:50 - 14:50 Section 3
    - RDS(MySQL), DynamoDB Overview
    - Lab 2: Lambda - extract data from RDS(MySQL) and load to S3 as csv file
- 14:50 - 15:00 Afternoon Break
- 15:00 - 16:00 Section 4
    - Lab 3: Lambda - read csv from S3 bucket, transform from csv to JSON format and load data into DynamoDB
    - Summary and Feedback