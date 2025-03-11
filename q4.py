# Question 4 (Optional - may require AWS Free Tier account)
# Log Analysis and Alerting
# This assignment tests your AWS and Python data engineering skills by building a simplified log analysis and alerting system.

# Scenario:

# You have a single application generating logs. You need to monitor these logs for specific error messages and trigger alerts when they occur.

# Requirements:

# Log Ingestion: Simulate a log stream (e.g., a Python script generating log entries). Each log entry should be a JSON string with a "message" field.

# Real-time Processing: Use AWS Lambda to process these log entries in real-time. The Lambda function should:

# Parse the JSON log entry.
# Check if the "message" field contains a specific error string (e.g., "ERROR_CODE_123").
# Alerting: If the error string is found, trigger an alert. For simplicity, just print a message to the console (CloudWatch Logs) indicating an alert has been triggered. You don't need to integrate with an external alerting service.

# Infrastructure as Code: Use the AWS CDK (Python) to define the Lambda function and any necessary supporting resources (e.g., an SQS queue if you want to decouple ingestion and processing, though this is optional for the simplified version).

# Testing: Provide a script to generate sample log entries and demonstrate how to trigger the alert.

# Documentation: Include a README explaining your design and how to run the test script.

# Simplified Example Log Entry:

# {"message": "Application started successfully."}


import json
import random
import time
import boto3
from datetime import datetime

# Instantiating the s3 client to interact with it
bucket_name = "ha-logs"
s3_client = boto3.client("s3")

log_messages = {
    "success": {
        "status_code": 200,
        "message": "Success! Operation completed successfully."
    },
    "warning": {
        "status_code": 300,
        "message": "Warning! High memory usage"
    },
    "error": {
        "status_code": 500,
        "message": "Error! Database connection failed"
    }
}

# this function triggers the put action in s3 for a given object in the given bucket 
def save_to_s3(log_data):
    file_name = f"logs/{datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=log_data)

# this function generates the random log messages set a bove
def generate_log():
    while True:
        current_type = random.choice(list(log_messages.keys()))
        log_entry = {
            "status_code": log_messages[current_type]["status_code"],
            "message": log_messages[current_type]["message"],
            "timestamp": datetime.utcnow().isoformat()
        }
        log_json = json.dumps(log_entry)
        print(log_json)
        save_to_s3(log_json)
        time.sleep(2)  

if __name__ == "__main__":
    generate_log()