import boto3
from boto3.dynamodb.conditions import Key

dynamoDB = boto3.resource('dynamodb')
task_table = dynamoDB.Table("meister_task_submited")

def lambda_handler(event, context):
    task_name = event['task_name']
    class_name = event['class_name']

    response = dynamodb_query_item(task_name, class_name)

    # TODO implement
    return {
        'statusCode': 200,
        'body': response
    }

def dynamodb_query_item(task_name: str, class_name: str):
    response = task_table.query(
        KeyConditionExpression=Key('task_name').eq(task_name) & Key('belongings').begins_with(class_name)
    )
    return response.get('Items', [])