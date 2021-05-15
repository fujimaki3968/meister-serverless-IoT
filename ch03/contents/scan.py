import boto3

dynamoDB = boto3.resource('dynamodb')
sample_table = dynamoDB.Table("meister_chapter03_tutorial")

def lambda_handler(event, context):
    response = dynamodb_scan_items()

    foods = list(map(lambda x: x['food'], response))

    # TODO implement
    return {
        'statusCode': 200,
        'body': foods.join(',')
    }

def dynamodb_scan_items():
    response = sample_table.scan()
    return response.get('Items', [])