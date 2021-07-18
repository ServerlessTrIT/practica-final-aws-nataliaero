import json
import boto3
import os

def handler(event, context):
    code = 200
    body = {}
    headers = {
        "Access-Control-Allow-Credentials": True,
        "Access-Control-Allow-Origin": "*",
    }

    if event['body'] is None:
        code = 400
    else:
        activator = json.loads(event['body'])
        activation_code = activator.get('code', '')
        email = activator.get('username', '')

        client = boto3.client('cognito-idp')
        try:
            result = client.confirm_sign_up(ClientId=os.environ['CLIENT_ID'], Username=email, ConfirmationCode=activation_code)
            body = {
                "message": "Usuario activado"
            }
        except Exception as e:
            code = 400

            body = {
                "message": e.args[0]
            }


    return {
        'statusCode': code,
        'headers': headers,
        'body': json.dumps(body)
    }