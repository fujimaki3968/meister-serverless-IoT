from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

time = datetime.now(JST)

print(time)
print(time.hour)

def lambda_handler(event, context):

    # TODO implement
    return {
        'statusCode': 200,
        'body': "午後・午前"
    }