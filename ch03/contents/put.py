import boto3

dynamoDB = boto3.resource('dynamodb')
sample_table = dynamoDB.Table("meister_chapter03_tutorial")

def lambda_handler(event, context):
    student_number = event['student_number']
    food = event['food']

    dynamodb_put_item(student_number, food)

    # TODO implement
    return {
        'statusCode': 200,
        'body': 'success'
    }


def dynamodb_put_item(id: str, food: str):
    field_params = {
        'id': id,
        'food': food
    }

    sample_table.put_item(
        Item=field_params
    )
