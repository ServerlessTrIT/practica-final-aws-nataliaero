import json
import boto3

def handler(event, context):
    book = json.loads(event['body'])
    headers = {
        "Access-Control-Allow-Credentials": True,
        "Access-Control-Allow-Origin": "*",
    }
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
        "headers": json.dumps(headers),
        "statusCode": result['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(body)
    }

    return response
