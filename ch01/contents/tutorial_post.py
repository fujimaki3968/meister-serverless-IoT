import json

def lambda_handler(event, context):
    name = event['name']
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello {0}!'.format(name))
    }
