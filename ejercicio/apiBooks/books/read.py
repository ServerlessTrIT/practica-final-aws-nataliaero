import json
import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BooksTable')

    if event['pathParameters'] is None:
        result = table.scan()
        items = result.get('Items', [])
        body = {
            'items': items
        }
    else:
        isbn = event['pathParameters']['id']
        key = {
            "isbn":isbn
        }
        result = table.get_item(Key=key)
        item = result.get('Item', {})
        body = {
            'item': item
        }

    response = {
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET',
        },
        "statusCode": result['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(body)
    }

    return response
