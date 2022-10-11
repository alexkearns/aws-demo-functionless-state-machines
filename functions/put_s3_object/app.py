import json
import boto3

s3 = boto3.resource("s3")


def lambda_handler(event, context):
    """Sample Lambda function which puts an object to an S3 bucket

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        dict: the response from the PutObject API call
    """
    object = s3.Object(
        bucket_name=event["bucket"],
        key=f"{event['uuid']}-merged.json"
    )
    
    response = object.put(
        Body=json.dumps(event["body"])
    )

    return response
