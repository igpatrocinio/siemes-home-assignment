# DISW Take-Home Assignment - Q4  #

## How to reproduce it

1 - Create a s3 bucket with the standard configuration
2 - Change the bucket_name in line 37 from the q4 script
3 - Create a lambda function with the following configuration:
    - Code as same as the lambda.py. Save and deploy the changes after pasting
    - Add a trigger for the lambda to be trigger when happens a PUT event in the bucket (the same one as specificed in step1)
    - Increase timeout for at least 10s
    - Add S3 ReadOnlyAccess to the lambda role
4 - Create the access keys for the AWS user who is testing
5 - Configure the AWS CLI using the credentials from the step below
6 - Execute the Script q4.py. Stop the Execution after seeing all types of operations (success, warning, error)
7 - Check the logs in CloudWatch Logstream 