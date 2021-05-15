import boto3

dynamoDB = boto3.resource('dynamodb')
sample_table = dynamoDB.Table("meister_chapter03_tutorial")

def dynamodb_put_item(id: str, title: str):
    field_params = {
        'id': id,
        'title': title
    }

    sample_table.put_item(
        Item=field_params
    )


def dynamodb_get_item(id: str):
    response = sample_table.get_item(
        Key={
            'id': id
        }
    )
    return response.get('Item', False)


def dynamodb_scan_items():
    response = sample_table.scan()
    return response.get('Items', [])