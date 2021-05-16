import boto3

dynamoDB = boto3.resource('dynamodb')
sample_table = dynamoDB.Table("meister_chapter03_tutorial")

def lambda_handler(event, context):
    student_number = event['student_number']

    dynamodb_delete_item(student_number)

    # TODO implement
    return {
        'statusCode': 200,
        'body': 'delete success'
    }

def dynamodb_delete_item(id: str):
    sample_table.delete_item(
        Key={
            'id': id
        }
    )