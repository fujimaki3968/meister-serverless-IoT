def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']

    # TODO implement
    return {
        'statusCode': 200,
        'body': 'Hello {0} {1}さん'.format(first_name, last_name)
    }
