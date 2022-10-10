from uuid import uuid4


def lambda_handler(event, context):
    """Sample Lambda function which generates a V4 UUID.

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        str: a UUIDv4 string
    """
    return str(uuid4())
