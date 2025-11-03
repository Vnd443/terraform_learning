import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    
    if http_method == 'GET':
        return retrieve_and_save_to_s3(event, context)
    elif http_method == 'POST':
        return modify_data(event, context)
    elif http_method == 'DELETE':
        return remove_data(event, context)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported method')
        }

def retrieve_and_save_to_s3(event, context):
    table_name = 'my-table'
    bucket_name = 'my-bucket-vnd'
    
    # Retrieve data from DynamoDB
    table = dynamodb.Table(table_name)
    response = table.scan()
    data = response['Items']
    
    # Save data to S3
    s3.put_object(Bucket=bucket_name, Key='data.json', Body=json.dumps(data))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data saved to S3')
    }

def modify_data(event, context):
    table_name = 'my-table'
    
    # Sample data for modification
    sample_items = [
        {
            'id': '123',
            'name': 'Sample Item 1',
            'description': 'This is the first sample item.'
        },
        {
            'id': '124',
            'name': 'Sample Item 2',
            'description': 'This is the second sample item.'
        },
        {
            'id': '125',
            'name': 'Sample Item 3',
            'description': 'This is the third sample item.'
        }
    ]
    
    items_to_put = []

    # Check if body is present in the event
    if 'body' in event and event['body']:
        try:
            item = json.loads(event['body'])
            if isinstance(item, list):
                items_to_put = item
            else:
                items_to_put.append(item)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }
    else:
        items_to_put = sample_items  # Use sample data if no body is provided
    
    # Modify data in DynamoDB
    table = dynamodb.Table(table_name)
    for item in items_to_put:
        table.put_item(Item=item)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data modified successfully')
    }

def remove_data(event, context):
    table_name = 'my-table'
    
    # Sample key for deletion
    sample_key = {
        'id': '123'
    }
    
    # Check if body is present in the event
    if 'body' in event and event['body']:
        try:
            key = json.loads(event['body'])
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid JSON format')
            }
    else:
        key = sample_key  # Use sample key if no body is provided
    
    # Remove data from DynamoDB
    table = dynamodb.Table(table_name)
    table.delete_item(Key=key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data removed successfully')
    }
