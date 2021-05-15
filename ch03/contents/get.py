import boto3

dynamoDB = boto3.resource('dynamodb')
sample_table = dynamoDB.Table("meister_chapter03_tutorial")

def lambda_handler(event, context):
    student_number = event['student_number']

    response = dynamodb_get_item(student_number)

    if response == False:
        return {
            'statusCode': 404,
            'body': 'data does not exist'
        }

    # TODO implement
    return {
        'statusCode': 200,
        'body': response['food']
    }


def dynamodb_get_item(id: str):
    response = sample_table.get_item(
        Key={
            'id': id
        }
    )
    return response.get('Item', False)
