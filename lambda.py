import json
import boto3
import logging

logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        try:
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            content = response['Body'].read().decode('utf-8')
            contents_json = json.loads(content)
            status_code = contents_json.get("status_code")
            message = contents_json.get("message")

            if status_code == 500:
                logging.error(f"An error has occurred")
                raise Exception(f"Operation failed: {message}")

        finally:
            logging.info(f"Operation completed successfully")

    
    return {
        'statusCode': status_code,
        'body': json.dumps(message)
    }