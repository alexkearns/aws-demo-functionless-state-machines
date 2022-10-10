import json

def lambda_handler(event, context):
    """Lambda function which merges two serialized JSON objects
    and returns it deserialized.

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        dict: the unserialized merged version of the JSON file
    """
    left = event["left"]
    right = event["right"]

    return {**left, **right}