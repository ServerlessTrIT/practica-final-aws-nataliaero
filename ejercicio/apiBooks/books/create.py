import json
import boto3

def handler(event, context):
    book = json.loads(event['body'])
    item = {
        "isbn":book['isbn'],
        "title":book['title']
    }

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BooksTable')
    result = table.put_item(Item=item)


    body = {
        "message": "create",
        "input": book
    }

    response = {
        "statusCode": result['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(body)
    }

    return response
