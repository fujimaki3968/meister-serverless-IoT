import boto3
import json
import datetime

dynamoDB = boto3.resource('dynamodb')

attendance_list = dynamoDB.Table("meister_attendance_list")

def lambda_handler(event, context):
    if 'student_number' in event:
        return return_error("学籍番号がありません。")
    elif 'name' in event:
        return return_error("名前がありません。")
    
    if not is_attendance:
        attendance(event['student_number'], event['name'])
    
    return {
        'statusCode': 200,
        'body': '{0}さんの出席が完了しました。'.format(event['name'])
    }

def return_error(message: str):
    return {
        'statusCode': 400,
        'message': message
    }

def attendance(student_number: int, name: str):
    now = datetime.datetime.now().timestamp()
    attendance_list.put_item(
        Item={
            'student_number': student_number,
            'name': name,
            'created': now
        }
    )

def is_attendance(student_number: int):
    response = attendance_list.get_item(
        Key={
            'student_number': student_number
        }
    )
    print(response)
    if 'Item' in response:
        return True
    else:
        return False