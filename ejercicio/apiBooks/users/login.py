import json
import boto3
import os

def handler(event, context):
    code = 200
    body = {}

    if event['body'] is None:
        code = 400
    else:
        user = json.loads(event['body'])
        email = user.get('username', '')
        password = user.get('password', '')

        ap = {
            "USERNAME": email,
            "PASSWORD": password
        }

        client = boto3.client('cognito-idp')
        try:
            result = client.initiate_auth(AuthFlow='USER_PASSWORD_AUTH', AuthParameters=ap, ClientId=os.environ['CLIENT_ID'])
            body = {
                "token": result['AuthenticationResult']['IdToken']
            }
        except Exception as e:
            code = 400
            body = {
                "message": e.args[0]
            }

    return {
        'statusCode': code,
        'body': json.dumps(body)
    }
