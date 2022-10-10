import os
import boto3

TABLE_NAME = os.environ["TABLE_NAME"]

ddb = boto3.resource("dynamodb")
table = ddb.Table(TABLE_NAME)


def lambda_handler(event, context):
    """Sample Lambda function which downloads a JSON file from S3
    and returns its contents

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        dict: the response from the PutItem API call
    """
    item = {
        "id": event["id"],
        **event["item"]
    }
    
    response = table.put_item(
        Item=item
    )

    return response
