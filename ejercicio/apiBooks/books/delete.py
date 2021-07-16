import json
import boto3

def handler(event, context):
    book = json.loads(event['body'])
    key = {
      "isbn":book['isbn']
    }

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BooksTable')
    result = table.delete_item(Key=key)


    body = {
        "message": "delete",
        "input": book
    }

    response = {
        "statusCode": result['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(body)
    }

    return response