import pytest
import json
from unittest.mock import patch, MagicMock
from lambda_function import lambda_handler, modify_data, remove_data

def test_lambda_handler_post():
    event = {
        'httpMethod': 'POST',
        'body': json.dumps({
            'id': '126',
            'name': 'Sample Item 4',
            'description': 'This is the fourth sample item.'
        })
    }
    context = {}
    
    with patch('lambda_function.dynamodb') as mock_dynamodb:
        # Mock the DynamoDB table put_item response
        mock_table = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        
        response = lambda_handler(event, context)
        print(response)
        print('POST Response Status Code:', response['statusCode'])
        print('POST Response Body:', response['body'])


def test_lambda_handler_delete():
    event = {
        'httpMethod': 'DELETE',
        'body': json.dumps({
            'id': '126'
        })
    }
    context = {}
    
    with patch('lambda_function.dynamodb') as mock_dynamodb:
        # Mock the DynamoDB table delete_item response
        mock_table = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        
        response = lambda_handler(event, context)
        print('DELETE Response Status Code:', response['statusCode'])
        print('DELETE Response Body:', response['body'])

def test_lambda_handler_unsupported_method():
    event = {'httpMethod': 'PUT'}
    context = {}
    
    response = lambda_handler(event, context)
    print('Unsupported Method Response Status Code:', response['statusCode'])
    print('Unsupported Method Response Body:', response['body'])

def test_modify_data_invalid_json():
    event = {
        'httpMethod': 'POST',
        'body': 'invalid json'
    }
    context = {}
    print('\n')
    print(response)
    print('\n')
    response = modify_data(event, context)
    print('Invalid JSON Modify Response Status Code:', response['statusCode'])
    print('Invalid JSON Modify Response Body:', response['body'])

def test_remove_data_invalid_json():
    event = {
        'httpMethod': 'DELETE',
        'body': 'invalid json'
    }
    context = {}
    
    response = remove_data(event, context)
    print('Invalid JSON Remove Response Status Code:', response['statusCode'])
    print('Invalid JSON Remove Response Body:', response['body'])

if __name__ == "__main__":
    test_lambda_handler_post()
    test_lambda_handler_delete()
    test_lambda_handler_unsupported_method()
    test_modify_data_invalid_json()
    test_remove_data_invalid_json()

