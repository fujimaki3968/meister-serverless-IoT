import boto3
import json
import datetime
import math

dynamoDB = boto3.resource('dynamodb')

attendance_list = dynamoDB.Table("meister_attendance_list")

def lambda_handler(event, context):
    if not 'student_number' in event.keys():
        return return_error("学籍番号がありません。")
    elif not 'name' in event.keys():
        return return_error("名前がありません。")
    elif not 'belongs' in event.keys():
        return return_error("所属が記入されていません。")
    
    if not is_attendance(event['student_number']):
        attendance(event['student_number'], event['name'], event['belongs'])
    else
        return_error("すでに出席しています。")
    
    return {
        'statusCode': 200,
        'body': '{0}さんの出席が完了しました。'.format(event['name'])
    }

def return_error(message: str):
    return {
        'statusCode': 400,
        'message': message
    }

def attendance(student_number: int, name: str, belongs: str):
    now = datetime.datetime.now().timestamp()
    attendance_list.put_item(
        Item={
            'student_number': student_number,
            'name': name,
            'belongs': belongs,
            'created': int(math.floor(now))
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