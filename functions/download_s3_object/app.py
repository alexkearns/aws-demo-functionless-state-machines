import json
import boto3


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
        dict: the unserialized version of the JSON file
    """
    s3 = boto3.resource("s3")
    object = s3.Object(
        bucket_name=event["bucket"],
        key=event["key"]
    )

    serialized_contents = object.get()
    contents = json.load(serialized_contents["Body"])

    return contents
