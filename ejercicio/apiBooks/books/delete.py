import json
import boto3

def handler(event, context):
    book = json.loads(event['body'])
    headers = {
        "Access-Control-Allow-Credentials": True,
        "Access-Control-Allow-Origin": "*",
    }
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
        "headers": json.dumps(headers),
        "statusCode": result['ResponseMetadata']['HTTPStatusCode'],
        "body": json.dumps(body)
    }

    return response